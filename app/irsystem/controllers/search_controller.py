from . import *  

import numpy as np
import pandas as pd

from app.irsystem.models.helpers import *
from app.irsystem.models.helpers import NumpyEncoder as NumpyEncoder

project_name = "Forever 4.300: Beauty Product Recommendation System"
net_id = "HaiYang Bai (hb388),\
		  Helen Liang (hl973),\
		  Joseph Kuo (jk2288)],\
		  Yue Gao (yg98),\
		  Zidong Zheng (zz357)"

# open csv files
cleanser_db = pd.read_csv('data/cleanser_db.csv')
eye_care_db = pd.read_csv('data/eye_care_db.csv')
lip_treatment_db = pd.read_csv('data/lip_treatment_db.csv')
masks_db = pd.read_csv('data/masks_db.csv')
moisturizer_db = pd.read_csv('data/moisturizer_db.csv')
sun_care_db = pd.read_csv('data/sun_care_db.csv')
treatment_db = pd.read_csv('data/treatment_db.csv')

# TODO: organize and process data

@irsystem.route('/', methods=['GET'])
def search():
	# get search parameters
	query = request.args.get('search')
	category = request.args.get('category')
	price_range = request.args.get('price_range')
	# TODO: add search parameters

	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)



