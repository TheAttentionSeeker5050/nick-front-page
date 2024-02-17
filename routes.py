# have the routes here
from flask import Blueprint

# import render_template
from flask import render_template
# impor request object
from flask import request

# import environment variables
import os

# import the get_all_links function
from data.link_data import get_all_links

# import the client from the app
from pymongo.mongo_client import MongoClient

main_bp = Blueprint('/', __name__)

# get the collection from the database
# Connect to MongoDB using environment variables
mongoClient = MongoClient(os.environ.get('MONGO_ADDRESS'))
db = mongoClient.frontPageDB
collection = db.links



@main_bp.route('/')
def index():
    # if get 
    if request.method == 'GET':

        # get all the links
        links = get_all_links(db)

        # filter the links by category
        social_links = [link for link in links if link['category'] == 'social']
        project_links = [link for link in links if link['category'] == 'project']

        # render the index.html
        return render_template('index.html', social_links=social_links, project_links=project_links)
    else:
        return render_template('invalid_method.html')


@main_bp.route('/invalid_method')
def invalid_method():
    return render_template('invalid_method.html')