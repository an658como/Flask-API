from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    # The regular return value is html
    # return "Hello World!"
    
    # For proper API you need to return json format and you need to provide a serializable data like dictionary to jsonify
    return jsonify({"about" : "Hellow World!"})



if __name__=='__main__':
    app.run(debug=True)