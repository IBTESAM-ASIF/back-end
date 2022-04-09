from itsdangerous import base64_decode, base64_encode
import openai

class model:

    key = open('api_key.txt','r')

    keys = key.readlines()

    encoded = keys[4].strip()

    openai.api_key = bytes.fromhex(encoded).decode('utf-8')

    def getSentimentAndKeywords(self, tweet):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Decide whether this Tweet's sentiment is: joy, fear, sadness, disgust, or anger, and tell me the keywords that caused it\n\nExamples\n\nTweet: \"I don't either. Its depressing. I don't think I even want to know about the kids in suitcases. \"\nSentiment: sadness\nKeywords: depressing\n\nTweet:\"SHOOTING OUTSIDE MY HOUSE :O NOT KIDDING! So SCARED\"\nSentiment: fear\nKeywords: SHOOTING, SCARED\n\nTweet:\"Gym attire today was: Puma singlet, Adidas shorts.......and black business socks and leather shoes  Lucky did not run into any cute girls.\"\nSentiment: joy\nKeywords: attire, cute, girls, \n\nTweet:\"didn't get shit done today ~ i'm so screwed\"\nSentiment: anger\nKeywords: shit, screwed, done\n\nTweet:\"{thistweet}\"\n".format(thistweet=tweet),
        temperature=0,
        max_tokens=40,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
        )
        return response.get("choices")[0]['text'].strip().lower()

    def is_Tweet_Questionable(self, tweet): #tweet text preprocessed and ready

        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Decide whether a Tweet's sentiment is unprofessional or fine\n\nExamples:\n\nTweet: \"I don't either. Its depressing. I don't think I even want to know about the kids in suitcases. \"\nSentiment: unprofessional\n\nTweet: \"Bad news was Dad has cancer and is dying   Good news new business started and  I am now a life coach practising holistic weight management\"\nSentiment: unprofessional\n\nTweet: \"SHOOTING OUTSIDE MY HOUSE :O NOT KIDDING! So SCARED\"\nSentiment: unprofessional\n\nTweet: \"Gym attire today was: Puma singlet, Adidas shorts.......and black business socks and leather shoes  Lucky did not run into any cute girls. \"\nSentiment: unprofessional\n\nTweet: \"Damn! The grind is inspirational and saddening at the same time.  Don't want you to stop cuz I like what u do! Much love,\"\nSentiment: fine\n\nTweet: \"didn't get shit done today ~ i'm so screwed\"\nSentiment: unprofessional\n\nTweet:\"{thetweet}\"\nSentiment".format(thetweet=tweet),
        temperature=0,
        max_tokens=40,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
        )
        if "fine" in response.get("choices")[0]['text'].strip().lower():
            return False
        else:
            return True