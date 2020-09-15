from flask import after_this_request, request
from flask import Flask, render_template
from flask_restful import Api, Resource
import logging
import sys, os
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
app = Flask(__name__)
# from xgboost import XGBClassifier

@app.route("/")
def hello():
    print("Hello World through print")
    logging.info("Hello World through logging")
    # return render_template('home.html')
    return "Hello World"

@app.route("/test")
def test():
    try:
        import pyaudio
        logging.info("done")
        return "success"
    except Exception as e:
        logging.error("Error: "+str(e))
        return "error:"+str(e)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=3000)
    # comment43

