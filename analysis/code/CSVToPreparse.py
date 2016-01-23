# This code isolates the tweets from data/tweetData.csv that have prelabeled sentiment,
# and puts them in a format suitable for transformation into .ptb
import csv, re, string

# unigrams obtained from short, opinionated tweets:
bullishUnigrams = ["long","bullish","nice","buy","boom","wow","very"," added","in","yes"
                   "breakout","green","today","holding","soon","pop"]
bearishUnigrams = ["short","bearish","sell"]

def annotateUnigrams(tweet, outfile, noPunct):
    words = tweet.split(' ')
    normalWords = [noPunct.sub('', word).lower() for word in words]
    for i in range(len(words)):
        if normalWords[i] in bullishUnigrams:
            outfile.write("4 " + words[i] + "\n")
        elif normalWords[i] in bearishUnigrams:
            outfile.write("0 " + words[i] + "\n")
        elif words[i] is not '':
            outfile.write("2 " + words[i] + "\n") # 1 grams are likely to be neutral
    outfile.write("\n") # extra line tells parser utterance is finished

with open('../data/tweetData.csv','r') as infile:
    reader = csv.reader(infile)
    reader.next() # skip header
    with open('../data/preParse.txt','w') as outfile:
        noPunct = re.compile('[%s]' % re.escape(string.punctuation))
        for row in reader:
            sentiment = row[8]
            if sentiment: # skip unlabeled tweets
                tweet = row[7]
                if re.match("\d", tweet[0]) is not None:
                    print tweet[0]
                    words=tweet.split(' ')
                    tweet=' '.join(words[1:len(words)]) # circumvent bug in parser

                if sentiment == 'bullish':
                    outfile.write("4 " + tweet + "\n") # map to 4
                    annotateUnigrams(tweet,outfile, noPunct)
                if sentiment == 'bearish':
                    outfile.write("0 " + tweet + "\n") # map to 0
                    annotateUnigrams(tweet,outfile, noPunct)
