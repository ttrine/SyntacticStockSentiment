import scrapy

class userData(scrapy.Item):
	userName 	 = scrapy.Field()
	ideas 		 = scrapy.Field()
	numFollowers = scrapy.Field()
	numFollowing = scrapy.Field()
	following 	 = scrapy.Field()

class tweetData(scrapy.Item):
	# user metadata
	userName 		   = scrapy.Field()
	userID 			   = scrapy.Field()
	isSuggested 	   = scrapy.Field()
	isInvestorRelation = scrapy.Field()

	# tweet (meta)data
	date 			   = scrapy.Field()
	time 			   = scrapy.Field()
	tweetID 		   = scrapy.Field()
	tweetBody 		   = scrapy.Field()
	sentiment 		   = scrapy.Field()
	totalLikes 		   = scrapy.Field()
	likesList 		   = scrapy.Field()
	totalReshares 	   = scrapy.Field()
	mentionedUsers 	   = scrapy.Field()
	replyTo 		   = scrapy.Field()
