#Imports Tweepy module, Time module, and Random module
import tweepy, time, random

#Declaring variables with API keys for readability purposes
consumerKey = '' #Insert your own API key within the quotation marks
consumerSecret = '' #Insert your own API key within the quotation marks
accessKey = '' #Insert your own API key within the quotation marks
accessSecret = '' #Insert your own API key within the quotation marks

#Authenticaton using vatiables declared above and Tweepy module
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

#Opens file containing possible answers and stores each line in a list called "answer"
with open('answers.txt') as line:
    answer = line.readlines()

#Asks for ID of last reply to avoid replying more than once
lastID = input("Please enter the last reply ID: ")
print("Bot is now live")

#Declares an infinite loop that repeats the proccess every minute
isOn = 1
while (isOn == 1):

    #Uses Tweepy API to look for recent mentions and stores them in a list called mentions
    mentions = api.mentions_timeline(since_id = lastID)

    #Declares a for loop to reply to every mention
    for mention in mentions:

        #Generates a random number which will serve as the index of the answer that will be delivered
        answerNum = random.randrange(0,len(answer))

        #Gathers user's @handle
        userName = mention.user.screen_name
        #Generates tweet with user's @handle and random answer
        tweetAnswer = ("@" + userName + " " + answer[answerNum])
        #Uses Tweepy API to tweet the previusly generated status update
        tweet = api.update_status(tweetAnswer, mention.id)
        #Saves last reply ID to avoid replying more than once
        lastID = mention.id

    #Delays the loop by 60 seconds to avoid exeeding Twitter's restrictions
    time.sleep(60)
