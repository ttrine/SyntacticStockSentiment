import scrapy
from stockTwitsGraph.items import userData

class userDataSpider(scrapy.Spider):
    name = "userData"
    allowed_domains = ["stocktwits.com"]
    start_urls = ["http://stocktwits.com/RedDogT3/following"]

    def parse(self, response):
        pageNum = response.xpath( # returns an array
            '//div[@class="pagination"]/em[@class="current"]/text()'
        ).extract()
        
        if len(pageNum) == 0 or pageNum[0] == '1': # record user stats, init Following array
            stats = response.xpath(
                '//ul[@id="traderStats"]/li/a/span/text()'
            ).extract()

            data = userData()
            userName = response.url.split('/')[3]
            data['userName'] = response.url.split('/')[3]
            data['ideas'] = int(stats[0].replace(',',''))
            data['numFollowers'] = int(stats[1].replace(',',''))
            data['numFollowing'] = int(stats[2].replace(',',''))


            data['following'] = []
        else: # pull data from previous request
            data = response.meta['data']

        usersOnPage = response.xpath(
            '//li[@class="message clearfix"]/div[@class="message-content"]/a/text()'
        ).extract()
        for user in usersOnPage: data['following'].append(user)
        
        nextPage = response.xpath(
            '//div[@class="pagination"]/a[@class="next_page"]/@href'
        ).extract()
        if nextPage:
            request = scrapy.Request(response.urljoin(nextPage[0]))
            request.meta['data'] = data
            yield request
        else:
            yield data
            for userName in data['following']:
                    yield scrapy.Request("http://stocktwits.com/"+userName+"/following")
