from flask import Flask, jsonify, request
from flask_restful import Resource, Api
app = Flask(__name__)
# Define a new api by inheriting from the app object
api = Api(app)


# When you want to properly use the api object instead of routes, we use classes to define the methods
# The classes inherit the Resource class from the flask_restful

class HelloWorld(Resource):
    def get(self):
        return {'about' : 'Hello World!'}

    def post(self):
        some_json = request.get_json()
        return {'you sent' : some_json}, 201


class Multi(Resource):
    def get(self, num):
        return {'result' : num*10}

class InChI(Resource):
    def get(self, inchi):
        return {'InChI' : inchi}

# Now that the classes are defined, it's time to add routes to the api using the add_resource method
# This is basically specifying the endpoints
api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')
api.add_resource(InChI, '/inchi/<string:inchi>')

if __name__=='__main__':
    app.run(debug=True)