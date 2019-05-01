from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import csv
import sys
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

f = open('scooter_tweets.csv', 'w')
writer = csv.writer(f)
writer.writerow(["id","created_at","text"])

alltweets = tweepy.Cursor(api.search, q='scooter').items()
for tweet in alltweets:
 #print(str(tweet).translate(non_bmp_map))
 # outtweets = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
 outtweets = [tweet.id_str, tweet.created_at, tweet.text]
 writer.writerow(outtweets)
 print(outtweets)
f.close()
