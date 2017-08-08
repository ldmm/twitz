import tweepy
import random
import time
from chomsky import chomsky

# provide your credentials
consumer_key 		= ""
consumer_secret 	= ""
access_token 		= ""
access_token_secret = "" 
hashtag 			= "#foo"

# create bot
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

"""
n = random.randint(1,100)
print "Generating %d tweets" % (n)
for i in range(n):
"""
counter = 0
while True:
	#generate tweets
	temp = []
	tuits = []
	for i in range(1000):
		temp.append( chomsky(1) + ' #dhsi2013')

	for t in temp:
		if len(t) <=140:
			tuits.append(t)

	random.shuffle(tuits)
	api.update_status(tuits[0])
	counter = counter + 1
	print "-------------------"
	print counter
	print tuits[0]

	#generating a slight pause	
	sleepTime = random.randint(60, 480)
	print "Waiting %d seconds" % (sleepTime)  
	time.sleep(sleepTime) 
	print "-------------------"

	
