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
	query = request.args.get('search')
	if not query:
		data = []
		output_message = ''
	else:
		output_message = "Your search: " + query
		data = range(5)
	return render_template('search.html', name=project_name, netid=net_id, output_message=output_message, data=data)



