from flask import Flask
# import os

app = Flask(__name__)
# apiKey = os.environ.get("MYAPIKEY")



@app.route('/')
def home():
    return "Hello, World!"


# @app.route("/about")
# def about(): 
#     return apiKey


