# This code separates tweets from data/tweetData.csv that have prelabeled sentiment

import csv

with open('../data/tweetData.csv','r') as infile:
	reader = csv.reader(infile)
	reader.next() # skip header
	with open('../data/labeled.txt','w') as labeled:
		labeledWriter = csv.writer(labeled)
		with open('../data/unlabeled.txt','w') as unlabeled:
			unlabeledWriter = csv.writer(unlabeled)
			for row in reader:
				sentiment = row[8]
				if sentiment: labeledWriter.writerow(row)
				else: unlabeledWriter.writerow(row)
