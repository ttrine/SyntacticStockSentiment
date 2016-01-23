# This code isolates tweets for estimating model accuracy

import csv

with open('../data/labeled.txt','r') as labeled:
	reader = csv.reader(labeled)
	with open('../data/splitDict.txt','r') as split:
		with open('../data/labeledTweets.txt','w') as labeledTweets:
			for row in reader:
				keyval = split.readline()
				tweet = row[7]
				if keyval.split(":")[1] == "test\n":
					labeledTweets.write(tweet + "\n")
