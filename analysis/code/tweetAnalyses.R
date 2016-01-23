library(plyr)

tweetData <- read.csv("~/Documents/stockMartket/analysis/data/tweetData.csv", stringsAsFactors=FALSE)
tweetDataSentiment140 <- read.csv("~/Documents/stockMartket/analysis/data/tweetDataSentiment140.csv", stringsAsFactors=FALSE)
userStats <- read.csv("~/Documents/stockMartket/analysis/data/userStats.csv", stringsAsFactors=FALSE)

tweetData$sentiment <- ifelse(tweetData$sentiment == "bullish",1,       # sentiment to int
                       ifelse(tweetData$sentiment=="bearish",-1,Inf))

tweetData$numWords <- sapply(strsplit(tweetData$tweetBody," +"),length) # count words

switch <- function(r) return(paste(r[3],r[2],r[1],sep="-"))             # fix date encoding
year <- function(r) return(as.integer(r[1]))
day <- function(r) return(as.integer(r[3]))
month <- function(r) return(as.integer(r[2]))

tweetData$date <- sapply(strsplit(tweetData$date,'-'),switch)
tweetData$year <- sapply(strsplit(tweetData$date,'-'),year)
tweetData$day <- sapply(strsplit(tweetData$date,'-'),day)
tweetData$month <- sapply(strsplit(tweetData$date,'-'),month)

sen140<-tweetDataSentiment140[,c("tweetID","sentiment140")]             # add sentiment140
tweetData <- merge(tweetData,sen140,by="tweetID",all.tweetData=FALSE,all.sen140=FALSE)

tweetData <- tweetData[tweetData$year == 2015,] # only recent tweets

# extract list of stock tickers
tweetData$tickers <- sapply(rapply(mapply(strsplit,MoreArgs=.(" "), # horrendus
                     lapply(strsplit(gsub('[[:punct:]]', '',
                    toupper(tweetData$tweetBody)),"CASHTAG"),
                     function(l) l[0:-1])),function(r) r[1], how="list"),
                     function(r) unlist(r)[unlist(r)!=""&is.na(as.integer(unlist(r)))])

linkFollowers<-function(row) userStats$numFollowers[userStats$username == row]
sapply(tweetData$userName,linkFollowers)[1:10]

onlySentiment <- tweetData[tweetData$sentiment!=Inf,]         # isolate labeled tweets

plot(table(tweetData$numWords),xlab="Number of words",ylab="Frequency",
     main="Distribution of Word Counts")

plot(table(tweetData$year),xlab="Year",ylab="Frequency",main="Distribution of Post Year")

remNeutral <- function(s) s[s!="LINKREPLACE" & !grepl('CASHTAG',s,fixed=TRUE)]
onlySentiment$filteredWords <- sapply(sentimentWords, remNeutral)
onlySentiment$filteredWordLens <- sapply(onlySentiment$filteredWords,length)

singles <- onlySentiment[onlySentiment$filteredWordLens==1,]
singles$normalized <- gsub('[[:punct:]]', '', tolower(singles$filteredWords))

composite <- ddply(singles,c("normalized"),summarize, # aggregate by normalized wordcount
                   frequency=length(sentiment),
                   mean=sum(sentiment)/length(sentiment),
                   stddev=sd(sentiment),
                   se=stddev/sqrt(frequency)
)
composite <- composite[composite$normalized!="",] # ignore frequency of blanks
composite <- composite[with(composite, order(-frequency)), ] # sort descending
plot(composite$frequency[1:200],composite$se[1:200],
     xlab="Frequency of Isolated Occurrence",
     ylab="Standard Error",
     main="Convergence of Sentiment for Common Words"
) # shows non-controversiality of high-frequency words

tweetData$hasAAPL <- grepl("AAPL",tweetData$tickers,)
tweetData$hasAMZN <- grepl("AMZN",tweetData$tickers,)

arbDay <- tweetData[tweetData$month=="6" & tweetData$day=="12",]
arbDay$userID <- as.factor(arbDay$userID)
arbDay$hasAAPL <- as.factor(arbDay$hasAAPL)
byDay <- ddply(arbDay,c("userID","hasAAPL"),summarise, # aggregate by normalized wordcount
    userSentimentAAPL <- sum(sentiment140)/count(sentiment140)
)


