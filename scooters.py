from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import csv
import sys
import time

#consumer key, consumer secret, access token, access secret.
ckey="FUijOiOMRBIKrbo2jB2FsnHNn"
csecret="VNfSUNsQX64x7p6CIFnbXSruBXVDANuzCEjLNxS1rVsdcMkXOY"
atoken="3020280138-Z54ovfJf8h00abEHORFq1q0ppwLB3GMSNBWomNq"
asecret="uVmTrmKD7ocwytn9VErU6J3wDdgLhJp5pRG2lzJTWm4Fr"
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

#emoji may give trouble when printing (not saving) so creating a translation table
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def scrape(input):
    query = str(input)

    f = open('tweets_' + query + '.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(["id","created_at","text","retweet_count"])
    # ,"favorite_count","user.followers_count"])

    # q="scooter", since="2019-04-24", until="2019-04-25"

    alltweets = tweepy.Cursor(api.search, q=query, since="2019-04-24", until="2019-04-25").items()
    for tweet in alltweets:
        # print(tweet)
        #  print(str(tweet).translate(non_bmp_map))
         outtweets = [tweet.id_str, tweet.created_at, tweet.text, tweet.retweet_count]
        # , tweet.favorite_count, tweet.user.followers_count]
         writer.writerow(outtweets)
         print(outtweets)

    f.close()
    # time.sleep(60 * 15)

# 15 minutes
# scrape("scooter")
# try:
# scrape("lime scooter")
# except:
# scrape("limebike")
#
#     try:
# scrape("bird scooter")
#     except:
# scrape("birdride")
#
#         try:
# scrape("jump scooter")
#         except:
# scrape("jumpbyuber")
# scrape("uber scooter")
# scrape("scootergang")
# scrape("scooter gang")
# scrape("escooter")
# scrape("limescooters")
# scrape("birdscooters")
scrape("jumpscooter")
scrape("jumpscooters")
# scrape("electricscooter")
# scrape("")