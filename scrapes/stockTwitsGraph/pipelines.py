# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class StocktwitsgraphPipeline(object):

    def process_item(self, item, spider):
    	#WRITE CODE TO KEEP ONLY ITEMS WITH A 'FOLLOWING' LIST
    	return item