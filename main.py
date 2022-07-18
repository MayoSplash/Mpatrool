from flask import Flask
from flask_restful import Api, Resource
import vk_api

app = Flask(__name__)
api = Api(prefix='/api')

accsess_token = "9845b98b9845b98b9845b98b6e983ec12d998459845b98bfa5ac65ed421762106e3abf0"
session = vk_api.VkApi(token=accsess_token)
vk = session.get_api()

class Wall(Resource):
    def get(self, id):
        res = vk.wall.get(owner_id=id)
        return res

class Account(Resource):
    def get(self, id):
        res = vk.users.get(user_id=id)
        return res



api.add_resource(Wall, "/wall/<int:id>")
api.add_resource(Account, "/user/<int:id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)


