from distutils.log import debug
from flask import Flask
from flask import render_template

from model import model
gpt3 = model()
from tweet import tweetGetter
tweeter = tweetGetter()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/connect")
def connect():
    return render_template('connect.html')


def preprocess_tweet(tweet):
    words = tweet.split(" ")
    for w in words:
        if "https:" in w or "@" in w:
            words.pop(words.index(w))
        
    return " ".join(c for c in words if c.isalpha())

@app.route("/results")
def results():
    results = "<h1>Results</h1>"
    user = "thelazyaz"
    response = tweeter.get_tweets(user,10)#[tweetobjects]
    for r in response:
        print(r.text)
        if(gpt3.is_Tweet_Questionable(preprocess_tweet(r.text)) == True):
            link = "https://twitter.com/" + user + "/status/" + r.id_str
            results += "<ul> <a href=" +"\"{l}\"".format(l=link)  + ">" + r.text + "</a> : " + gpt3.getSentimentAndKeywords(preprocess_tweet(r.text)) + "</ul>"

    return results

if __name__ == '__main__':
  
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)