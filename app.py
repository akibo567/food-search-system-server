from flask import *
import requests
from flask_cors import CORS
import json

from settings import API_KEY,CORS_ORIGIN

app = Flask(__name__)
CORS(app, origins=CORS_ORIGIN, methods=["POST"])
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():

    return "This Is Backend System."

@app.route("/search_shop", methods=["POST"])
def search_shop():
    page_count = int(request.json["Page_Item_Amount"])

    url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    param = { 
        "key": API_KEY,
        "format": "json",
        "count": page_count,
        "start": ( (request.json["Current_Pageno"] - 1) * page_count) + 1,
        "lat": request.json["Latitude"],
        "lng": request.json["Longitude"],
        "range": request.json["Range"],
        "keyword": request.json["Keyword"],
        "private_room": request.json["Private_Room"],
        "parking": request.json["Parking"],
        "budget": request.json["Budget"],
        "lunch": request.json["Lunch"],
        "midnight_meal": request.json["Midnight_Meal"],
        }
    
    if request.json["Budget"] != "":
        param["budget"] = request.json["Budget"]
    
    res = requests.get(url, params=param)
    res_json = res.json()
    res_array = []


    for jsonObj in res_json["results"]["shop"]:
        res_array.append(
            {
                "name":jsonObj["name"],
                "acccess":jsonObj["access"],
                "thumb_img":jsonObj["logo_image"],
                "location":jsonObj["address"],
                "business_hour":jsonObj["open"],
                "name_kana":jsonObj["name_kana"],
                "catch":jsonObj["catch"],
                "close":jsonObj["close"],
                "private_room":jsonObj["private_room"],
                "parking":jsonObj["parking"],
                "party_capacity":jsonObj["party_capacity"],
                "budget_average":jsonObj["budget"]["average"],
                "urls_pc":jsonObj["urls"]["pc"],
                "coupon_urls_pc":jsonObj["coupon_urls"]["pc"],
                "coupon_urls_sp":jsonObj["coupon_urls"]["sp"],
                "capacity":jsonObj["capacity"],
            }
        )

    return {
                "shop":res_array,
                "results_available":res_json["results"]["results_available"],
        }

@app.route("/budget_list", methods=["POST"])
def budget_list():

    url = "http://webservice.recruit.co.jp/hotpepper/budget/v1/"
    param = { 
        "key": API_KEY,
        "format": "json",
        }
    
    res = requests.get(url, params=param)
    res_json = res.json()
    res_array = []


    for jsonObj in res_json["results"]["budget"]:
        res_array.append(
            {
                "code":jsonObj["code"],
                "name":jsonObj["name"],
            }
        )

    return {"budget":res_array}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)