#!/usr/bin/env python3
# Post-El0n proto2 - still using twikit
# I made ChatGPT refactor it to implement asyncio (new hotness), and it worked! 
# What a world we live in.

import asyncio
import datetime
import logging
import random
import os
from twikit import Client

# configure logging
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='/var/log/automatli.log', level=logging.INFO, format=log_format)

# account info
USERNAME = "INPUT YOUR USERNAME HERE"
EMAIL = "ACCOUNTEMAIL@PROVIDER.TLD"
PASSWORD = "YOUR-P4SSW0RD"

client = Client('en-US')

async def login():
    if os.path.exists('cookies.json'):
        client.load_cookies('cookies.json')
    else:
        await client.login(auth_info_1=USERNAME, auth_info_2=EMAIL, password=PASSWORD)
        client.save_cookies('cookies.json')

async def load_data(file_path):
    return await asyncio.to_thread(lambda: open(file_path, 'r').readlines())

async def generate_tweet(IC, IP, SP, TP, FD):
    ICinter = random.choice(IC) if random.randrange(1, 6) < 5 else ""
    FDinter = random.choice(FD) if random.randrange(1, 6) <= 4 else ""
    return str.lower(ICinter.strip()) + str.lower(random.choice(IP).strip()) + \
           str.lower(random.choice(SP).strip()) + str.lower(random.choice(TP).strip()) + \
           str.lower(FDinter.strip())

def calculate_next_tweet_time(minutes_until_next_tweet):
    current_time = datetime.datetime.now()
    next_tweet_time = current_time + datetime.timedelta(minutes=minutes_until_next_tweet)
    return next_tweet_time.strftime("%Y-%m-%d %H:%M:%S")

async def main():
    await login()
    
    IC, IP, SP, TP, FD = await asyncio.gather(
        load_data('./IC.txt'), load_data('./IP.txt'), load_data('./SP.txt'), 
        load_data('./TP.txt'), load_data('./FD.txt')
    )
    
    while True:
        tweet = await generate_tweet(IC, IP, SP, TP, FD)
        print(f"Tweeting: {tweet}")
        logging.info(f"Tweeting: {tweet}")
        await client.create_tweet(tweet)

        tweet_frequency = random.randint(1620, 13370)
        print(f"Next tweet in ~{round(tweet_frequency / 60)} minutes, at {calculate_next_tweet_time(round(tweet_frequency / 60))}")
        logging.info(f"Next tweet in ~{round(tweet_frequency / 60)} minutes, at {calculate_next_tweet_time(round(tweet_frequency / 60))}")

        await asyncio.sleep(tweet_frequency)

asyncio.run(main())
