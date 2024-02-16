from flask import Flask
from pymongo import MongoClient

# import the routes
from routes import main_bp

# download environment variable handler
from dotenv import load_dotenv, find_dotenv
import os

# initialize the Flask app
app = Flask(__name__)

# register the routes
app.register_blueprint(main_bp)

# Load environment variables from .env file
load_dotenv(find_dotenv())

print(os.environ.get('MONGO_ADDRESS'))

# Connect to MongoDB using environment variables
client = MongoClient(os.environ.get('MONGO_ADDRESS'))
db = client.frontPageDB

# Define your routes and other Flask application logic here

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')