from . import *  
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from .data import product_dict, category_dict, brand_dict
from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "Forever 4.300: Beauty Product Recommendation System"
net_id = "HaiYang Bai (hb388),\
		  Helen Liang (hl973),\
		  Joseph Kuo (jk2288)],\
		  Yue Gao (yg98),\
		  Zidong Zheng (zz357)"

@irsystem.route('/', methods=['GET'])
def search():
	# get search parameters
	query = request.args.get('search')
	brand = request.args.get('brand')
	category = request.args.get('category')
	price_range = request.args.get('price_range')
	skin_concern = request.args.get('skin_concern')
	skin_type = request.args.get('skin_type')
	
	# Filter products by query category and brand 
	filtered_products_id = set(product_dict.keys())
	if str(category) != 'all_categories':
		filtered_products_id = filtered_products_id.intersection(set(category_dict[category]))
	if str(brand) != 'all_brands':
		filtered_products_id = filtered_products_id.intersection(set(brand_dict[brand]))
				
	# Vectorize product data along with product ID for cosine sim
	filtered_products_id = list(product_dict.keys())
	filtered_products = [product_dict[prod_id] for prod_id in filtered_products_id]
	filtered_prod_reviews = []
	if str(skin_type) == 'all_skin_types':
		for product in filtered_products:
			concat_review = ''
			for review in product.reviews:
				concat_review = concat_review + review.text
			filtered_prod_reviews.append(concat_review)
	else:
		# only consider reviews of query skin type or no skin type
		for product in filtered_products:
			concat_review = ''
			for review in product.reviews:
				if review.skin_type == skin_type or review.skin_type == '':
					concat_review = concat_review + review.text
			filtered_prod_reviews.append(concat_review)
	
	# Use skin_concerns as query into the cosine sim search
	filtered_products_id.insert(0, 'query')
	filtered_prod_reviews.insert(0, str(skin_concern))

	vectorizer = TfidfVectorizer(max_features=5000, stop_words='english', max_df=0.8, min_df=10, norm='l2')
	prod_by_vocab = vectorizer.fit_transform(filtered_prod_reviews).toarray()

	# Run Cosine Sim
	result_ids = cosine_sim(filtered_products_id, prod_by_vocab)

	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)


"""
Returns a sorted list of product ID most similar to query
"""
def cosine_sim(filtered_products_id, tfidf_mat):
	result = [0] # similarity with itself is 0
	for i in range (1, len(tfidf_mat)):
		score = np.dot(tfidf_mat[0], tfidf_mat[i])
		result.append(score)
	if len(result) < 21:
		sorted_idx = list(np.argsort(result))[::-1][:len(result)-1]
	else:
		sorted_idx = list(np.argsort(result))[::-1][:20]
	product_ids = [filtered_products_id[idx] for idx in sorted_idx]
	if 'query' in product_ids:
		product_ids.remove('query')
	return product_ids

"""
filtered_products_id = set(product_dict.keys())
filtered_products_id = filtered_products_id.intersection(set(category_dict['moisturizer']))
filtered_products_id = list(product_dict.keys())
filtered_products = [product_dict[prod_id] for prod_id in filtered_products_id]
filtered_prod_reviews = []
for product in filtered_products:
	concat_review = ''
	for review in product.reviews:
		concat_review = concat_review + review.text
	filtered_prod_reviews.append(concat_review)
filtered_products_id.insert(0, 'query')
filtered_prod_reviews.insert(0, 'hydrating, spf, brightening, whitening, refreshing')

vectorizer = TfidfVectorizer(max_features=5000, stop_words='english', max_df=0.8, min_df=10, norm='l2')
prod_by_vocab = vectorizer.fit_transform(filtered_prod_reviews).toarray()

# Run Cosine Sim
result_ids = cosine_sim(filtered_products_id, prod_by_vocab)
print(result_ids)
"""
