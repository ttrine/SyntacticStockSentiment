import json,csv

def main():
	jsonData = []

	with open("userDataAll.json",'r') as rawFile:
		File = rawFile.read()
		jsonData = json.loads(File)

	with open("userStats.csv",'w') as csvFile:
		writer = csv.writer(csvFile)
		writer.writerow(['username','numPosts','numFollowers','numFollowing'])
		for user in jsonData:
			if (user['ideas'] >= 5 	 and	# require a minimum amount
			user['numFollowers'] >= 5 and	# of user engagement
			user['numFollowing'] >= 0):
				writer.writerow([
					user['userName'],
					user['ideas'],
					user['numFollowers'],
					user['numFollowing']])

if __name__ == '__main__':
	main()