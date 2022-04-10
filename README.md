# [Demo Here](https://eris-checker.herokuapp.com/)

## Inspiration
First impressions are a deciding factor when forming new relationships. However, in the professional world, your digital footprint is often your introduction to employers and potential connections. Something you posted years ago could easily ruin that first impression. Our generation is the first of its kind to grow up with social media around us. One platform we used as children is Twitter. As children, none of us had any regard to what we posted, so finding inappropriate Tweets you may have forgotten about are not uncommon.

As we transition into the workplace, things we said may come back to haunt us. Anyone can view your public profile and see what you post, but most users are not willing to private their account and limit their online presence. Our proposed solution would greatly assist anyone trying to make their transition to the workplace.

## Our Solution
We made Eris to help college students transition to their professional careers. Eris helps find your unprofessional tweets before your employer does. It does so with our integrated AI program, which uses sentiment analysis on your past tweets to evaluate them. Our AI then generates a dashboard that displays analytics on any past, unprofessional tweets to help you prepare your digital presence for finding a job. In the end though, the user is given the power to delete their tweets. Eris simply enables users to easily find those unprofessional tweets and identify how they might seem to others.

## The Model We Chose
Our group chose GPT3 as it is the state-of-the-art natural language processing model that allows us to conduct semantic analysis. Through semantic analysis, we would be able to identify whether a tweet is professional or not, helping our program reach its goal in helping students.

For each tweet, we ask our model: “Decide whether this Tweet is: questionable or fine”. For each questionable/unprofessional tweet we then asked it the following question: “Decide whether this Tweet's sentiment is: joy, fear, sadness, disgust, or anger, and tell me the keywords that caused it”. Our AI then outputs the 5 emotion sentiments of the questionable tweet and the keywords that caused the tweet to be flagged as unprofessional.

## Training the Model
Training the model was an important step in integrating our AI. Without past precedent to go off of, how would our model know what to even classify as unprofessional in the first place. Our team decided to create an initial dataset in order to train our model for test cases. To create a balanced dataset with minimal bias, tweets were randomly selected from the twitter api, and then classified as questionable, unprofessional, or neither by our team. Of the questionable and unprofessional tweets they were classified from the main emotion each tweet has and the keywords in the tweet that caused it

GPT3 by default performs a wide variety of NLP tasks, called few-shot learning. To further tune it to our two specific sentiment classification tasks, we utilized this aspect of GPT3. In addition, training GPT3 results in: higher quality results, rate limit savings, and lower latency requests. All of these improvements helped make our user experience as smooth as possible.

## Challenges We Ran Into
There were many challenges our team ran into when creating Eris. Challenges ranged from trouble integrating the API with our AI to fundamental aspects of the program. One of those aspects was the goal of the project. Our group truly believed in using sentiment analysis to describe tweets. As a result, our original goal was to analyze a user’s mental health based on the sentiments of their tweet. This goal had to be changed though as we dove further into our research. After speaking with a psychology professor at Drexel, we realized that the quality of mental health is too complex to classify based on tweets alone. We transitioned our project goal to focus more on detecting tweets that could jeopardize someone’s professional career as a result. This led us to develop our AI to focus more on the extreme feelings that are emulated from certain tweets which are often considered unprofessional.

After we finalized our project goal, we continued working on the program. Along the way, we ran into many other challenges we had to overcome. We discovered that implementing user authentication through the Twitter API is more complex than our group originally found out to be. At first, we wanted to implement it by recreating an HTTP signature to request authentication from the API, but the process quickly became too complicated. We then tried to host it through firebase, but setting this service up required a paid subscription to connect it to our javascript code. Eventually, we settled on having the user input their Twitter username to our program, and then giving a code for the user to Tweet, so our program can identify the user’s account.

One smaller challenge we had was finding Training data for the AI in an unbiased way. Rather than try to create our own dataset for the AI, which could possibly be biased or incorrect, we randomly pulled multiple tweets from Twitter’s API. This method allowed us to give obvious judgment on whether a tweet was unprofessional and teach it to the AI.

## Most Notable Aspects
Our GPT-3 model outputs high quality responses with minimal training data. This reduces the risk of the model misclassifying an unprofessional tweet or the emotions or keywords of said tweet. Our User Interface also has a very clean design that helps the user navigate the website in a time efficient manner, and make it easy to understand what about the displayed tweets made them unprofessional.

## What's Next for Eris
Our team expects to increase the scale of Eris in the future. Our scale would increase by scope as we plan to have our AI branch out and analyze other social media platforms through web scraping or APIs. Our AI could also be improved upon to allow it to analyze and judge images from posts. Finally, we can make Eris more accessible by integrating it into a Google chrome extension.
