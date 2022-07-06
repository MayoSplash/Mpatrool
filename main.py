#9845b98b9845b98b9845b98b6e983ec12d998459845b98bfa5ac65ed421762106e3abf0
import json

from flask import Flask
from flask_restful import Api, Resource
import requests
import vk_api

app = Flask(__name__)
api = Api()

#session = vk_api.VkApi(login="89883451024", password="Cucumber_2")
session = vk_api.VkApi(token="9845b98b9845b98b9845b98b6e983ec12d998459845b98bfa5ac65ed421762106e3abf0")
vk = session.get_api()

class Main(Resource):
    def get(self, user_ids):
        res = vk.wall.get(owner_id=user_ids)
        return res

api.add_resource(Main, "/<int:user_ids>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)


