# This code isolates tweets for estimating model accuracy

import csv

with open('../data/labeled.txt','r') as labeled:
	reader = csv.reader(labeled)
	with open('../data/splitDict.txt','r') as split:
		with open('../data/labeledTweets.txt','w') as labeledTweets:
			writer = csv.writer(labeledTweets)
			for row in reader:
				keyval = split.readline()
				if keyval.split(":")[1] == "test\n":
					tweet = row[7]
					sentiment = row[8]
					if sentiment == "bullish": sentiNum = 1
					else: sentiNum = -1
					writer.writerow([tweet,sentiNum])
