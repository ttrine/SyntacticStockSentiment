userStats <- read.csv("~/Documents/stockMartket/graph/userStats.csv")
library(plyr)

#1: Count users across in-degree(number of followers) and out-degree(number following)
followersFollowing <- as.matrix(table(userStats$numFollowers,userStats$numFollowing))

#2: Compute the average number of posts for each user
postSum <- ddply(userStats, c("numFollowers", "numFollowing"), summarise,sumPosts = sum(numPosts))
a <- followersFollowing
i=1
for(r in as.integer(rownames(a))){
  j=1
  for(c in as.integer(colnames(a))){
    p <- postSum[postSum$numFollowers==r & postSum$numFollowing==c,3]
    a[i,j] <- ifelse(length(p)==1,p,0) / followersFollowing[i,j]
    j=j+1
  }
  j=1
  i=i+1
}
i=1

#3: Store result persistently because the computation takes forever
write(a,file="~/Documents/stockMartket/graph/heatMap.csv",sep=',')

#4: Plots
l<-log(followersFollowing)
l[l==-Inf] <- 0
filled.contour(l[1:25,1:100],
               color = heat.colors, nlevels=40,
               plot.title=title(
                 main="Followers vs. Following on StockTwits",
                 xlab="1 ≤ Number of Followers ≤ 25",
                 ylab="1 ≤ Number Following ≤ 100"),
               key.title=title(main="Log\n# Posts"),
               axes=FALSE
)

b <- a
logb <- log(b)
logb[logb==-Inf] <- 0
#logb[!is.finite(logb)] <- max(logb[is.finite(logb)])
filled.contour(logb[1:25,1:100],
               color = heat.colors, nlevels=40,
               plot.title=title(
                 main="Followers vs. Following on StockTwits",
                 xlab="1 ≤ Number of Followers ≤ 25",
                 ylab="1 ≤ Number Following ≤ 100"),
               key.title=title(main="Log\n# Posts"),
               axes=FALSE
)

a[103,100]#1548,30696