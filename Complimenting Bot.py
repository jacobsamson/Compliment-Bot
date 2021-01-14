'''
Jacob Samson
Date: 1/14/2021
Complimenting Bot

A twitter bot that replies to users that mention it in a tweet. It replies with
their name and a compliment.
'''

import tweepy
import random
import time

consumer_key = '1gWDXc3KIPeTkUDZowLKIDd4G'
consumer_secret = '9XMeNAsxY5S7Z6fD36bpJX6wkMzWD9NKU4YTxfnL0oQOe4sDRk'

key = '1332114509230604294-T17c7nuR0Mz92ISMTLWxrkYVKpSt4a'
secret = 'mWbyRQSTwvKfeCHkpxgq0B6lPTUTVN8SCFtXHnrcgA1aK'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

FILE_NAME = 'tweets_read.txt'

complimentList = [
                  "on a scale of 1 to 10, you're an 11",
                  "is there anything you can't do?",
                  "no one is quite like you. You're one of a kind!",
                  "have a great day!",
                  "you got this!",
                  "keep fighting the good fight!",
                  "I believe in you!"
                  ]

def read_last_seen(FILE_NAME):
    """
    Gives the id of the last read tweet
    
    :param FILE_NAME: .txt file containing previous tweet ID
    :return: the id of the last read tweet
    """
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
                     
def store_last_seen(FILE_NAME, last_seen_id):
    """
    Inputs the id of the last read tweet into FILE_NAME
    
    :param FILE_NAME:.txt file containing previous tweet ID
    :param last_seen_id: the id of the previously read tweet
    """
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 
                
def reply():
    """
    Tweets back at mentions with the user's name and a random compliment from complimentList
    """
    tweetMentions = api.mentions_timeline(read_last_seen(FILE_NAME))
    for i in reversed(tweetMentions):
        randomIndex = random.randint(0, len(complimentList))
        print("@" + i.user.screen_name + i.user.name + ", random index", i.id)
        api.update_status("@" + i.user.screen_name + " " + i.user.name + ", " + complimentList[randomIndex], i.id)
        store_last_seen(FILE_NAME, i.id)

while True:
    reply()
    time.sleep(30)
