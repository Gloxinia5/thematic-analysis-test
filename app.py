from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return requests.__version__
   

if __name__ == '__main__':
    app.run()