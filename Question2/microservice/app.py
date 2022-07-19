# save this as app.py
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
    return "Number summator healthy.", 200

@app.route("/sum", methods=['POST'])
def sum():
    try:
        if "value1" in request.form and "value2" in request.form and len(request.form) == 2:
            return "The value is: " + str( int(request.form['value1']) + int(request.form['value2']) ), 200
        else:
            raise Exception("ERROR - Request format error")
    except:
        return "An error occured, please try again later.", 500

