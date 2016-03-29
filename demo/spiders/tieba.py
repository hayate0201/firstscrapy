# -*- coding: utf-8 -*-
from scrapy.spider import Spider  
from scrapy.selector import Selector  
import os

class TiebaSpider(Spider):  
    name = "tieba"  
    allowed_domains = ["www.baidu.com"]
    start_urls = ["http://tieba.baidu.com/p/4427148943?pn=1"]
    def parse(self, response): 
		#print response.body
		#items = []
		for sel in response.xpath('//div[@class="l_post j_l_post l_post_bright  "]'):
			item = {}
			item['text'] = sel.xpath('//cc/div/text()').extract()
			#title = [n.encode('utf-8') for n in text]
			yield item
		#error spider must return request,baseItem,dict or none
