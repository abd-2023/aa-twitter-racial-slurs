import json
import re

# getting the json file of user tweet - simulating the result that would be given by twitter api
f = open("tweets.json")

# types of racial slurs given
racial_slurs = ["racial_slur", "an_racial_slur", "vn_racial_slur"]

# constructing regex string using the given list of racial slurs
racial_slurs_str = "|".join(racial_slurs)
print("racial_slurs_str", racial_slurs_str)

# converting all tweets in json file to python list
tweets = json.load(f)

# print("tweets type", type(tweets))

for tweet_info in tweets:
    # deg = 0 # degree of profanity
    # print("----------tweet-----------\n", tweet_info["tweet"])
    deg = len(re.findall(racial_slurs_str, tweet_info["tweet"]))
    print("tweet_info", tweet_info)

    #printing the degree of profanity out
    print("degree of profanity", deg)


f.close()