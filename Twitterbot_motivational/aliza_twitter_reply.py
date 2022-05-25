# -*- encoding: utf-8 -*-
# Description: Uses aiml for replying to tests
# Edited by: Rafael Sanchez
# April, 2022

import tweepy
import time
import os
import aiml

BRAIN_FILE="C:\\Users\\rafas\\Documents\\Github\\AI-Projects\\Lisa\\brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

#This initializes everything
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    global FILE_NAME
    global api
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        #print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id # Might need to recheck this
        store_last_seen_id(last_seen_id, FILE_NAME)
        new_text = list(mention.full_text.split(' '))
        for i in range(len(new_text)):
            if '@' in new_text[i]:
                new_text[i] = ''
        api.update_status('@' + mention.user.screen_name + " " + k.respond(' '.join(new_text).lower())[0:250], mention.id)


while True:
    # Replies to tweets that mention us
    reply_to_tweets()

    # Go to sleep
    time.sleep(15)
