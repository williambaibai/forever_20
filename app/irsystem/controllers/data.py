import os
import numpy as np
import pandas as pd

# open csv files
cleanser_db = pd.read_csv('data/cleanser_db.csv')
eye_care_db = pd.read_csv('data/eye_care_db.csv')
lip_treatment_db = pd.read_csv('data/lip_treatment_db.csv')
masks_db = pd.read_csv('data/masks_db.csv')
moisturizer_db = pd.read_csv('data/moisturizer_db.csv')
sun_care_db = pd.read_csv('data/sun_care_db.csv')
treatment_db = pd.read_csv('data/treatment_db.csv')
""" 
Class Representing the information of a product
"""
class Product:

  def __init__(self, name, brand, image, description, price, category):
    self.name = name
    self.brand = brand
    self.image = image
    self.description = description
    self.price = price
    self.category = category
    self.reviews = []

"""
Class Represetning the information of a review
"""
class Review:
  
  def __init__(self, text, rating, skin_type, skin_concerns):
    self.text = ''
    self.rating = 0
    self.skin_type = ''
    self.skin_concerns = ''

# organize data into 3 dictionaries
product_dict = {}
category_dict = {}
brand_dict = {}

def parse_category(category_name, db):
  for i in range(len(db.index)):
    product_id = str(db['product_id'][i])
    brand = str(db['brand'][i])
    # handle special case for price
    price_str = str(db['price'][i])
    if price_str.find('-') == -1:
      price = float(price_str[1:])
    else:
      price = float(price_str[1:price_str.find('-')])
    if product_id not in product_dict:
      product_dict[product_id] = Product(str(db['name'][i]), 
                                         brand,
                                         str(db['product_image_url'][i]),
                                         str(db['description'][i]),
                                         price,
                                         category_name
                                        )
      
      if category_name not in category_dict:
        category_dict[category_name] = [product_id]
      else:
        category_dict[category_name].append(product_id)

      if brand not in brand_dict:
        brand_dict[brand] = [product_id]
      else:
        brand_dict[brand].append(product_id)

    review = Review(str(db['review_text'][i]), 
                    int(str(db['rating'][i])),
                    str(db['skin_type'][i]), 
                    str(db['skin_concerns'][i])
                    )
    product_dict[product_id].reviews.append(review)

parse_category('cleanser', cleanser_db)
parse_category('eye_care', eye_care_db)
parse_category('lip_treatment', lip_treatment_db)
parse_category('masks', masks_db)
parse_category('moisturizer', moisturizer_db)
parse_category('sun_care', sun_care_db)
parse_category('treatment', treatment_db)

