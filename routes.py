# have the routes here
from flask import Blueprint

# import render_template
from flask import render_template
# impor request object
from flask import request

# import the get_all_links function
from data.link_data import get_all_links

main_bp = Blueprint('/', __name__)

@main_bp.route('/')
def index():
    # if get 
    if request.method == 'GET':

        links = get_all_links()
        social_links = [link for link in links if link['category'] == 'social']
        project_links = [link for link in links if link['category'] == 'project']

        # render the index.html
        return render_template('index.html', social_links=social_links, project_links=project_links)
    else:
        return render_template('invalid_method.html')


# @main_bp.route('/invalid_method')
# def invalid_method():
#     return render_template('invalid_method.html')