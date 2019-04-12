import os
import numpy as np
import pandas as pd

os.chdir('../../..')

# open csv files
cleanser_db = pd.read_csv('data/cleanser_db.csv')
#eye_care_db = pd.read_csv('data/eye_care_db.csv')
#lip_treatment_db = pd.read_csv('data/lip_treatment_db.csv')
#masks_db = pd.read_csv('data/masks_db.csv')
#moisturizer_db = pd.read_csv('data/moisturizer_db.csv')
#sun_care_db = pd.read_csv('data/sun_care_db.csv')
#treatment_db = pd.read_csv('data/treatment_db.csv')
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

# organize data into dictionaries
product_dict = {}
for i in range(len(cleanser_db.index)):
  product_id = str(cleanser_db['product_id'][i])
  if product_id not in product_dict:
    product_dict[product_id] = Product(str(cleanser_db['name'][i]), 
                                       str(cleanser_db['brand'][i]),
                                       str(cleanser_db['product_image_url'][i]),
                                       str(cleanser_db['description'][i]),
                                       float(str(cleanser_db['price'][i])[1:]),
                                       'cleanser'
                                       )
  review = Review(str(cleanser_db['review_text'][i]), 
                  int(str(cleanser_db['rating'][i])),
                  str(cleanser_db['skin_type'][i]), 
                  str(cleanser_db['skin_concerns'][i])
                  )
  product_dict[product_id].reviews.append(review)