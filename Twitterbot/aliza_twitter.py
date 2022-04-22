# -*- encoding: utf-8 -*-
# Description: Using markivify to recreate a markov chain bot Aliza, along with chatterbot functions
# Edited by: Rafael Sanchez
# April, 2022

import tweepy
import time
import numpy as np
import random
import datetime
import markovify
import sys
sys.path.append('C:\\Users\\rafas\\Documents\\Github\\AI-Projects\\Alizabot')
import brain

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

#This initializes everything
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

MIN_TIME = 21600
MAX_TIME = 86400

with open("corpus.txt", encoding="utf-8") as f:
    text = f.read()

# Source: https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

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
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')
    for mention in reversed(mentions):
        #print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        print("Replying to ", mention.user.screen_name)
        last_seen_id = mention.id # Might need to recheck this
        store_last_seen_id(last_seen_id, FILE_NAME)
        new_text = list(mention.full_text.split(' '))
        for i in range(len(new_text)):
            if '@' in new_text[i]:
                new_text[i] = ''
        api.update_status('@' + mention.user.screen_name + " " + brain.aliza_says(' '.join(new_text).lower(),'C:\\Users\\rafas\\Documents\\Github\\AI-Projects\\Alizabot\\brain.txt'), mention.id)


while True:
    # Likes messages regarding computers and/or universe and/or Lain Iwakura
    hashtags = "#lain #Lain #lainiwakura #LainIwakura #serialexperimentslain #SerialExperimentsLain #シリアルエクスペリメンツレイン #岩倉玲音" + "#lain #Lain #lainiwakura #LainIwakura #serialexperimentslain #SerialExperimentsLain #シリアルエクスペリメンツレイン #岩倉玲音" + "#lain #Lain #lainiwakura #LainIwakura #serialexperimentslain #SerialExperimentsLain #シリアルエクスペリメンツレイン #岩倉玲音" + "#lain #Lain #lainiwakura #LainIwakura #serialexperimentslain #SerialExperimentsLain #シリアルエクスペリメンツレイン #岩倉玲音" + " #computer #technology #pc #tech #gaming #laptop #computerscience #software #programming" + " #pcgaming #windows #coding #computers #gamer #apple #programmer #code" + " #developer #python #java #game #internet" + " #javascript #coder #gamingpc #linux #computerrepair #komputer #electronics #cybersecurity" + " #engineering #hardware #pcgamer #hp #android #hacker #intel #pcbuild #html" + " #hacking #lenovo #notebook #gamingsetup #pcmasterrace #setup #microsoft" + " #computer #technology #pc #tech #gaming #laptop #computerscience #software #programming #pcgaming"
    hash_list = hashtags.split(' ')
    tag_to_search = hash_list[random.randint(0, len(hash_list)-1)]
    tweets = api.search(tag_to_search)
    chosen_tweet_index = random.randint(0, len(tweets)-1)
    ID = tweets[chosen_tweet_index].id
    status = api.get_status(ID)
    favorited = status.favorited
    if favorited == False:
        api.create_favorite(ID)
        print("Tweet liked: " + tweets[chosen_tweet_index].text)

    # Follow people back
    new_followers = False
    print("People followed back: ")
    for follower in api.followers():
        friendship = api.show_friendship(source_screen_name = "aliza_bot", target_screen_name = follower.screen_name)
        if not friendship[0].following:
            new_followers = True
            follower.follow()
            print(follower.screen_name)
    if not new_followers:
        print("None")

    # Unfollow People
    people_unfollowed = False
    print("People unfollowed:")
    for friend in api.friends():
        friendship2 = api.show_friendship(source_screen_name = "aliza_bot", target_screen_name = friend.screen_name)
        if not friendship2[1].following:
            people_unfollowed = True
            api.destroy_friendship(friend.screen_name)
            print(friend.screen_name)
    if not people_unfollowed:
        print("None")

    # Generates the text
    text_model = markovify.Text(text)
    msg = text_model.make_short_sentence(random.randint(100, 280))
    api.update_status(msg)
    sleep_time = random.randint(MIN_TIME, MAX_TIME)
    current_time = datetime.datetime.now()
    print("Latest Status Update: " + str(current_time) + ".\nTime before next tweet: " + convert(sleep_time) + ".\nAliza said: '" + msg + "'")

    # Replies to tweets that mention us
    reply_to_tweets()

    print("Going to sleep for " + str(sleep_time) + " seconds.")
    print("*********************************************")
    # Go to sleep
    
    time.sleep(sleep_time)
