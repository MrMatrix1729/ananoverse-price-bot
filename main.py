import requests
import praw
import json
import time

reddit = praw.Reddit(
	user_agent="",
	client_secret="",
	client_id="",
	username="",
	password=""
)


def fileread(token):
	file1 = open(r"./test.txt", "r")
	pricesraw = file1.readlines()
	prices = [x[:-1] for x in pricesraw]

	if token == "ananos":
		return prices[0]
	elif token == "manangos":
		return prices[1]
	else:
		return "Error, Incorrect/Unsupported token!"


subreddit = reddit.subreddit("ananoverse")
for comment in subreddit.stream.comments(skip_existing=True):
	print(comment.body)
	if comment.body.startswith("convert"):
		splitedcom = comment.body.split()
		coin1price = int(float(fileread(splitedcom[2])))
		coin2price = int(float(fileread(splitedcom[3])))
		amount = int(splitedcom[1])
		finalamount = coin2price/coin1price*amount
		comment.reply(splitedcom[1] + " " + splitedcom[2] + " = " + str(finalamount) + " " + splitedcom[3] )
