from flask import *
import requests
from flask_cors import CORS

from settings import API_KEY

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], methods=["GET", "POST"])
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():

    return "This Is Backend System."

@app.route("/search_shop", methods=["POST"])
def search_shop():
    dummy_json =  [
        {
          "name":"ダミー1",
          "acccess":"HOGEから徒歩一分",
          "thumb_img":"hoge.jpg",
          "location":"A町B市",
          "business_hour":"8:00~18:00",
        },
        {
          "name":"ダミー2",
          "acccess":"HOGEから徒歩99分",
          "thumb_img":"hoge.jpg",
          "location":"A町B市",
          "business_hour":"8:00~18:00",
        },
        {
          "name":"ダミー3",
          "acccess":"HOGEから徒歩一分",
          "thumb_img":API_KEY,
          "location":"A町B市",
          "business_hour":"8:00~18:00",
        },
        {
          "name":"ダミー4",
          "acccess":"HOGEから徒歩一分",
          "thumb_img":"hogee.jpg",
          "location":"A町B市",
          "business_hour":"8:00~18:00",
        }
      ]
    return jsonify(dummy_json)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)