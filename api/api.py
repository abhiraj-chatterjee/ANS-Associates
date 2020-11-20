import time
from flask import Flask
from flask_cors import CORS
import pymongo
from bson import ObjectId, json_util
import json

app = Flask(__name__)

connectionURL = "mongodb+srv://abhiraj_chatterjee:paglaabu2001@ans-associates.2z78p.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(connectionURL)

brochure = client.get_database("Brochure")
# brochureCollection = brochure.brochureCollection

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


