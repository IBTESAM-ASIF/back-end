from distutils.log import debug
from flask import Flask
from flask import render_template

from model import model
myModel = model()
from tweet import tweetGetter
tweeter = tweetGetter()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connect")
def connect():
    return render_template('connect.html')


@app.route("/results")
def results():
    results = "<h1>Results</h1>"

    response = tweeter.get_tweets("Benjome1",10)#[tweetobjects]
    print(response)
    for r in response:
        print(r.text)        
    return results

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()