from itsdangerous import base64_decode, base64_encode
import openai

class model:

    key = open('api_key.txt','r')

    keys = key.readlines()

    encoded = keys[4].strip()

    openai.api_key = bytes.fromhex(encoded).decode('utf-8')

    def getKeywords(self, tweet):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Decide whether this Tweet's sentiment is: joy, fear, sadness, disgust, or anger, and tell me the keywords that caused it\n\nExamples\n\nTweet: \"I don't either. Its depressing. I don't think I even want to know about the kids in suitcases. \"\nKeywords: depressing\n\nTweet:\"SHOOTING OUTSIDE MY HOUSE :O NOT KIDDING! So SCARED\"\nKeywords: SHOOTING, SCARED\n\nTweet:\"Gym attire today was: Puma singlet, Adidas shorts.......and black business socks and leather shoes  Lucky did not run into any cute girls.\"\nTweet:\"didn't get shit done today ~ i'm so screwed\"\nKeywords: shit, screwed, done\n\nTweet:\"Love the flow of the hair\"\nKeywords: Love, flow, hair\n\nTweet:\"Humanity did not evolve to mourn the unborn\"\nKeywords: mourn, unborn\n\nTweet:\"Sustainable energy generation from sun & wind is making great progress!\"\nKeywords: Sustainable, energy, generation, sun, wind, progress\n\nTweet:\"{thistweet}\"".format(thistweet=tweet),
        temperature=0,
        max_tokens=40,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
        )
        return response.get("choices")[0]['text'].strip().lower()

    def getSentiment(self, tweet):
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Decide whether this Tweet's sentiment is: joy, fear, sadness, disgust, or anger\n\nExamples\n\nTweet: \"I don't either. Its depressing. I don't think I even want to know about the kids in suitcases. \"\nSentiment: sadness\nTweet:\"SHOOTING OUTSIDE MY HOUSE :O NOT KIDDING! So SCARED\"\nSentiment: fear\nTweet:\"Gym attire today was: Puma singlet, Adidas shorts.......and black business socks and leather shoes  Lucky did not run into any cute girls.\"\nSentiment: joy\nTweet:\"didn't get shit done today ~ i'm so screwed\"\nSentiment: anger\nTweet:\"Love the flow of the hair\"\nSentiment: joy\nTweet:\"Humanity did not evolve to mourn the unborn\"\nSentiment: disgust\nTweet:\"Sustainable energy generation from sun & wind is making great progress!\"\nSentiment: joy\nTweet:\"{thistweet}\"".format(thistweet=tweet),
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
        prompt="Decide whether a Tweet's sentiment is unprofessional or fine\n\nExamples:\n\nTweet:\"I don't either. Its depressing. I don't think I even want to know about the kids in suitcases. \"\nSentiment: unprofessional\n\nTweet: \"Bad news was Dad has cancer and is dying   Good news new business started and  I am now a life coach practising holistic weight management\"\nSentiment: unprofessional\n\nTweet: \"SHOOTING OUTSIDE MY HOUSE :O NOT KIDDING! So SCARED\"\nSentiment: unprofessional\n\nTweet: \"Gym attire today was: Puma singlet, Adidas shorts.......and black business socks and leather shoes  Lucky did not run into any cute girls.\"\nSentiment: unprofessional\n\nTweet: \"Damn! The grind is inspirational and saddening at the same time.  Don't want you to stop cuz I like what u do! Much love,\"\nSentiment: fine\n\nTweet: \"didn't get shit done today ~ i'm so screwed\"\nSentiment: unprofessional\n\nTweet:\"I wanted to attend something that's worth the price of a ticket :)\"\nSentiment: fine\n\nTweet:\"Join Pie & AI Bangalore ambassador, Rakesh Channaiah & experts from various startups who provide cloud-based solutions for AI to discuss the challenges.\"\nSentiment: fine\n\nTweet:\"Mother's Day is just around the corner Don't miss out and get the perfect gift ON TIME.\"\nSentiment: fine\n\nTweet:\"oh no...the thumbnails are leaking onto our desktops\"\nSentiment: fine\n\nTweet:\"Conversely, color jitter does not affect shape or texture-based categories (e.g. zebra), but affects color-based categories (like basket ball).\nStrangely, even weight decay affects different classes differently.\"\nSentiment: fine\n\nTweet: \"{thetweet}\"\nSentiment:".format(thetweet=tweet),
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