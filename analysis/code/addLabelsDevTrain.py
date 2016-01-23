
# This code adds labels to the training vectors produced by the RI-induced word space

import csv

with open('../data/labeled.txt', 'r') as labeled:
    reader = csv.reader(labeled)
    with open('../data/splitDict.txt','r') as split:
        with open("../data/trainDevDocumentVectors.out", 'r') as docVecs:
            with open('../data/labeledTrainDevDocVecs.csv', 'w') as out:
                i = 0
                for row in reader:
                    keyval = split.readline()
                    classLabel = keyval.split(":")[1]
                    if classLabel == "train\n" or classLabel == "dev\n":
                        sentiment = "1" if row[8] == "bullish" else "-1"
                        vector = docVecs.readline()
                        out.write(vector[1:-1] + sentiment + "\n")
