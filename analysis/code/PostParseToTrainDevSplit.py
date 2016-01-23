# This code randomly splits postParse.txt into train and dev files

import random

trainDevIndices = set(random.sample(range(1,78233), 62586))
trainIndices = set(random.sample(trainDevIndices,54762))

with open('../data/postParse.txt','r') as infile:
	with open('../data/splitDict.txt','w') as splits:
		with open('../data/train.txt','w') as train:
			with open('../data/dev.txt','w') as dev:
				with open('../data/test.txt','w') as test:
					lineNum = 1
					for line in infile.readlines():
						if lineNum in trainIndices: 
							train.write(line)
							splits.write(str(lineNum) + ":train\n")
						elif lineNum in trainDevIndices: 
							dev.write(line)
							splits.write(str(lineNum) + ":dev\n")
						else: 
							test.write(line)
							splits.write(str(lineNum) + ":test\n")
						lineNum=lineNum+1
