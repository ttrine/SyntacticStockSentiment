import csv

with open('../data/tweetData.csv','r') as infile:
	reader = csv.reader(infile)
	reader.next() # skip header
	with open('../data/justTweets.txt','w') as outfile:
		for row in reader:
			outfile.write(row[7] + "\n")
