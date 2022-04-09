from distutils.log import debug
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
import matplotlib.pyplot as plt
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
    """
    for tweet in tweets:
            if not tweet.text.isalpha():
                tweets.pop(tweets.index(tweet))"""
    correctCode = ""
    for r in response:
        correctCode = r.text

    count = 0
    quotes = []
    links = []
    feelings=[]
    keys = []

    if correctCode == c:
        response = tweeter.get_tweets(user,20)#[tweetobjects]
        for r in response:
            print(r.text)
            if(gpt3.is_Tweet_Questionable(preprocess_tweet(r.text)) == True):
                quotes.append(r.text)
                count +=1
                link = "https://twitter.com/" + user + "/status/" + r.id_str
                links.append(link)
                sentiment = gpt3.getSentiment(preprocess_tweet(r.text))
                keywords = gpt3.getKeywords(preprocess_tweet(r.text))
                
                s = sentiment.split(" ")[1:]
                s = " ".join(s)
                feelings.append(s)
                k = keywords.split(" ")[1:]
                k = " ".join(k)
                keys.append(k)

                joycount = 0
                fearcount = 0
                sadnesscount = 0
                disgustcount =0
                angercount = 0
                for z in feelings:
                    if(z.lower() == "joy"):
                        joycount += 1
                    elif(z.lower() == "fear"):
                        fearcount += 1
                    elif(z.lower() == "sadness"):
                        sadnesscount += 1
                    elif(z.lower() == "disgust"):
                        disgustcount += 1
                    elif(z.lower() == "anger"):
                        angercount += 1
                mylabels = { "Joy":joycount, "Fear":fearcount, "Sadness":sadnesscount, "Disgust":disgustcount, "Anger":angercount }
                names = [key for key,value in mylabels.items() if value!=0]
                values = [value for value in mylabels.values() if value!=0]

                fig = plt.figure()
                fig.patch.set_facecolor('#A85EE2')
                plt.pie(values, labels = names, autopct='%.1f%%')
                plt.rcParams.update({'text.color': "white"})
                plt.savefig('static/assets/img/examplepiechart.png')

                #\"{l}\"   .format(l=link)
                #results += "<tr> <td><a href=" +"\"#\""  + ">" + r.text + "</a> </td> <td>" + s + "</td> <td>" +k +"</td></tr>"
        #print(range(count))
        #print(quotes)
        #print(s)
        #print(k)
        #print(links)

        if count == 0:
            return render_template('results.html', flagged=True, isFlagged="No Flagged Tweets Found",theCount = range(count), allTweets=quotes, theFeelings=feelings, theKeys=keys, theLinks=links )


        return render_template('results.html', flagged=False, isFlagged="Flagged Tweets",theCount = range(count), allTweets=quotes, theFeelings=feelings, theKeys=keys, theLinks=links )
        
    else:
        #return redirect(url_for('connect', connect = c, Invalid="Your Account Could Not Be Verified, Try Again"))
        return connect(Invalid="Your Account Could Not Be Verified, Try Again")

if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)
