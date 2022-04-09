from distutils.log import debug
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import random

from model import model
gpt3 = model()
from tweet import tweetGetter
tweeter = tweetGetter()

app = Flask(__name__)

def getRandomCode():
    Verifycode = random.randint(10000000, 99999999)
    return str(Verifycode)

c = getRandomCode()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connect")
def connect(Invalid=""):
    return render_template('connect.html', connect = c, Invalid=Invalid)

def preprocess_tweet(tweet):
    words = tweet.split(" ")
    for w in words:
        if "https:" in w or "@" in w:
            words.pop(words.index(w))
        
    return " ".join(c for c in words if c.isalpha())

@app.route("/results",  methods=['POST'])
def results():
    user = request.form['username']
    response = tweeter.get_tweets(user, 1)
    correctCode = ""
    for r in response:
        correctCode = r.text
    if correctCode == c:
        results = "<h1>Results</h1>"
        response = tweeter.get_tweets(user,10)#[tweetobjects]
        for r in response:
            print(r.text)
            if(gpt3.is_Tweet_Questionable(preprocess_tweet(r.text)) == True):
                link = "https://twitter.com/" + user + "/status/" + r.id_str
                results += "<ul> <a href=" +"\"{l}\"".format(l=link)  + ">" + r.text + "</a> : " + gpt3.getSentimentAndKeywords(preprocess_tweet(r.text)) + "</ul>"

        return results
        
    else:
        #return redirect(url_for('connect', connect = c, Invalid="Your Account Could Not Be Verified, Try Again"))
        return connect(Invalid="Your Account Could Not Be Verified, Try Again")

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
