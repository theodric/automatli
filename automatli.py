#!/usr/bin/env python3
# automatli2024 post-Elon prototyp 2.1

import sys
import time
import datetime
import logging
import random
from pathlib import Path
from twikit import Client

## twikit login setup:
client = Client('en-US')

# Enter your account information here
# Uncomment and use this for the first login
USERNAME = "INPUT YOUR USERNAME HERE"
EMAIL = "ACCOUNTEMAIL@PROVIDER.TLD"
PASSWORD = "YOUR-P4SSW0RD"
#
client.login(
    auth_info_1=USERNAME,
    auth_info_2=EMAIL,
    password=PASSWORD
)
client.save_cookies('cookies.json')

# For the second+ login, comment out lines 16-25 inclusive and uncomment the line below:
# client.load_cookies('cookies.json')

ICraw = './IC.txt'
IPraw = './IP.txt'
SPraw = './SP.txt'
TPraw = './TP.txt'
FDraw = './FD.txt'
blank = ""

ICFile = open(ICraw, 'r')
IC = ICFile.readlines()
ICFile.close()

IPFile = open(IPraw, 'r')
IP = IPFile.readlines()
IPFile.close()

SPFile = open(SPraw, 'r')
SP = SPFile.readlines()
SPFile.close()

TPFile = open(TPraw, 'r')
TP = TPFile.readlines()
TPFile.close()

FDFile = open(FDraw, 'r')
FD = FDFile.readlines()
FDFile.close()
## Configure logging
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='/var/log/automatli.log', level=logging.INFO, format=log_format)

## Function to print the time of the next tweet
def calculate_next_tweet_time(minutes_until_next_tweet):
	current_time = datetime.datetime.now()
	next_tweet_time = current_time + datetime.timedelta(minutes=minutes_until_next_tweet)
	return next_tweet_time.strftime("%Y-%m-%d %H:%M:%S")

while True:
	ICidx = random.randrange(len(IC))
	IPidx = random.randrange(len(IP))
	SPidx = random.randrange(len(SP))
	TPidx = random.randrange(len(TP))
	FDidx = random.randrange(len(FD))

	ICinter = IC[ICidx]
	ICrand = random.randrange(1,6)
	if ICrand < 5:
		ICinter = ""

	FDinter = FD[FDidx]
	FDrand = random.randrange(1,6)
	if FDrand > 4:
		FDinter = ""

	tvit = str.lower(ICinter.rstrip("\r\n")) + str.lower(IP[IPidx].rstrip("\r\n")) + str.lower(SP[SPidx].rstrip("\r\n")) + str.lower(TP[TPidx].rstrip("\r\n")) + str.lower(FDinter.rstrip("\r\n"))
	print("Tweeting the following nonsense: " + tvit)
	logging.info("Tweeting the following nonsense: " + tvit)

	client.create_tweet(tvit)

	## You have two options for the below.
	## You should ONLY uncomment one of these!

	## Option 1: hardcode the frequency of tweets posted, in SECONDS
	## Don't set this too low, or you may get rate-limited, or even put in Twitter Jail!
	## Reminder: there are 3600 seconds in an hour, and 86400 seconds in a day.
#	tweetFrequency = 14400

	## Option 2: 
	## Have a timer which fires randomly within a range of intervals in SECONDS.
	## I recommend this, since it looks more like how a human would tweet, rather than
	## being on rails like a regular timer.
	tweetFrequency = random.randint(1620, 13370)
	
	print("Next tweet in approximately", round(tweetFrequency / 60), "minutes, at", calculate_next_tweet_time(round(tweetFrequency / 60)))
	logging.info("Next tweet in approximately %s minutes, at %s", round(tweetFrequency / 60), calculate_next_tweet_time(round(tweetFrequency / 60)))	

# I found the countdown in stdout annoying, so I replaced this function with the above, but it's still here if you want it.
#	for i in range(tweetFrequency, 0, -1):
#		time.sleep(1)
#		sys.stdout.write(str((i - 1))+' ')
#		sys.stdout.flush()

	time.sleep(tweetFrequency)
