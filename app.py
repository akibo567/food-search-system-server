from flask import *
import requests
from flask_cors import CORS
import json

from settings import API_KEY

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], methods=["GET", "POST"])
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():

    return "This Is Backend System."

@app.route("/test")
def test():
    url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    param = { 
        "key": API_KEY,
        "format": "json",
        "count": 5,
        "name": "うん",
        }
    

    res = requests.get(url, params=param)
    res_json = res.json()

    res_json_hairetu = []

    for jsonObj in res_json["results"]["shop"]:
        res_json_hairetu.append(jsonObj)

    return res_json_hairetu

@app.route("/search_shop", methods=["POST"])
def search_shop():
    url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    param = { 
        "key": API_KEY,
        "format": "json",
        "count": 5,
        "lat": request.json["Latitude"],
        "lng": request.json["Longitude"],
        "range": 2,
        #"name": request.json['name'],
        }
    
    res = requests.get(url, params=param)
    res_json = res.json()
    res_array = []


    for jsonObj in res_json["results"]["shop"]:
        res_array.append(
            {
                "name":jsonObj["name"],
                "acccess":jsonObj["address"],
                "thumb_img":jsonObj["logo_image"],
                "location":jsonObj["access"],
                "business_hour":jsonObj["open"],
            }
        )

    return res_array



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)