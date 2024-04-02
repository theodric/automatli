#!/usr/bin/env python3
# automatli public version 1

import time
import sys
from pathlib import Path
import random
from twikit import Client

## twikit login setup:
## don't comment out this line!
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

## Set frequency of tweets posted, in SECONDS
## Don't set this too low, or you may get rate-limited, or even put in Twitter Jail!
## Reminder: there are 3600 seconds in an hour, and 86400 seconds in a day.
tweetFrequency = 3600

## Sanity check.
if ACCESS_SECRET == 'unmodified':
    print("\nYou must first edit the script and configure a few well-labeled variables before you can use it.\n")
    exit()

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
	print("Next twot nonsense will be: " + tvit)

	client.create_tweet(tvit)

	for i in range(tweetFrequency, 0, -1):
		time.sleep(1)
##if you find the countdown in stdout annoying, remove the following two lines
		sys.stdout.write(str((i - 1))+' ')
		sys.stdout.flush()
