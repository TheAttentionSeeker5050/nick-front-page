from pymongo import MongoClient
from models.link_model import Link


# # import collection from the database
# client = MongoClient('mongo', 27017)
# client = MongoClient(os.environ.get('MONGO_ADDRESS'))
# db = client.frontPageDB
# collection = db.links


def create_link(db, link_label, link_url, link_icon_name, category):
    link = Link(link_label, link_url, link_icon_name, category)
    link_dict = link.to_dict()
    # collection.insert_one(link_dict)
    db.links.insert_one(link_dict)
    return link_dict

def get_all_links(db):
    # links = list(collection.find())
    links = list(db.links.find())
    return links
