from flask import Flask
from pymongo import MongoClient

# import the routes
from routes import main_bp

# download environment variable handler
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# initialize the Flask app
app = Flask(__name__)

# register the routes
app.register_blueprint(main_bp)

# app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))


# print(os.environ.get('MONGO_ADDRESS'))

# log the environment variable MONGO_ADDRESS
app.logger.info('MONGO_ADDRESS: ' + os.environ.get('MONGO_ADDRESS'))

# Connect to MongoDB using environment variables
client = MongoClient(os.environ.get('MONGO_ADDRESS'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Define your routes and other Flask application logic here

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')