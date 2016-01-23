# This code isolates tweets for generating word spaces

import csv

with open('../data/labeled.txt','r') as labeled:
	reader = csv.reader(labeled)
	with open('../data/splitDict.txt','r') as split:
		with open('../data/trainDevTweets.txt','w') as labeledTweets:
			for row in reader:
				keyval = split.readline()
				tweet = row[7]
				classLabel = keyval.split(":")[1]
				if classLabel == "train\n" or classLabel == "dev\n":
					labeledTweets.write(tweet + "\n")
