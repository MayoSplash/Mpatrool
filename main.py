from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self, user_id):
        return {"1": user_id}








api.add_resource(Main, "/<int:user_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=30)


