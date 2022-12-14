from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        if todo_id not in todos.keys():
            return {'error' : 'no todo item found with this id'} 
        else:
            return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['info']
        return {todo_id: todos[todo_id]}


# Here the endpoint is modified a bit        
api.add_resource(TodoSimple, '/todo/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)