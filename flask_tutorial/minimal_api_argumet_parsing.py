from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse




app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {'data' : 'Hello World! '+str(todo_id)}

    def put(self, todo_id):
        todos[todo_id] = request.form['info']
        return {todo_id: todos[todo_id]}
        

api.add_resource(TodoSimple, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
    parser = reqparse.RequestParser()
    parser.add_argument('rate', type=int, help='Rate to charge for this resource')
    args = parser.parse_args()