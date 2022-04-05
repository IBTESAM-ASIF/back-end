import openai

key = open('api_key.txt','r')

keys = key.readlines()

openai.api_key = keys[4].strip()



def classify_tweet_emotion(tweet):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Decide whether a Tweet's sentiment is: joy, fear, sadness, disgust, or anger\n\nTweet: \"" + tweet +"\"\nSentiment: ",
    temperature=0,
    max_tokens=20,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    return response

def is_Tweet_Questionable(tweet):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Decide whether a Tweet is: questionable, unprofessional, or neither\n\nTweet: \"" + tweet + "\"\nSentiment: ",
    temperature=0,
    max_tokens=14,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    if "neither" in response:
        return False
    else:
        return True