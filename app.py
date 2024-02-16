from flask import Flask
from pymongo import MongoClient

# import the routes
from routes import main_bp

# initialize the Flask app
app = Flask(__name__)

# register the routes
app.register_blueprint(main_bp)

# Connect to MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client.frontPageDB

# Define your routes and other Flask application logic here

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')