# -*- encoding: utf-8 -*-
# Description: Using markivify to recreate a markov chain bot Netgirl
# Edited by: Rafael Sanchez
# June 11, 2021

import tweepy
import time
import numpy as np
import random
import datetime
import markovify

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

#This initializes everything
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

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
        friendship = api.show_friendship(source_screen_name = "nettogirl", target_screen_name = follower.screen_name)
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
        friendship2 = api.show_friendship(source_screen_name = "nettogirl", target_screen_name = friend.screen_name)
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
    print("Latest Status Update: " + str(current_time) + ".\nTime before next tweet: " + convert(sleep_time) + ".\nNetgirl said: '" + msg + "'")
    print("*********************************************")
    # Go to sleep
    time.sleep(sleep_time)
