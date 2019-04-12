from . import *  
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
	
	# TODO: add search parameters

	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)



