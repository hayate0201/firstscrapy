# -*- coding: utf-8 -*-
#from scrapy.selector import Selector
import scrapy,json,codecs,time
from demo.items import BankItem
class AbcdSpider(scrapy.spiders.Spider):

	name = "abcd"
	allowed_domains = ["ewealth.abchina.com"]
	page = 1
	start_urls=[
		'http://ewealth.abchina.com/app/data/api/DataService/BoeProductV2?i=1&s=15&o=0&w=%E5%8F%AF%E5%94%AE|||||||1||0||']
	
	def __init__(self):
		self.page=1
		self.row=1
		#清空文件内容
		self.file = codecs.open('data/abc2.json', 'wb', encoding='utf-8')
		self.file.write("")
		
	def parse(self, response):
		
		#保存文件路径
		self.file = codecs.open('data/abc2.json', 'a', encoding='utf-8')
		sites = response.xpath('//NewDataSet/Table')
		datarows = response.xpath('//NewDataSet/Table1/total/text()').extract()
		#总数目
		sel = scrapy.Selector(response)
		total = sel.xpath('//Table1/total/text()').extract()[0] 
		total = int(total,10) #58
		
		#当前数目
			
		
		for site in sites:
			#定义Item
			item = BankItem()
			item['bank_code']		= "abc"
			item['bank_name'] 		= "农业银行"
			item['bank_type']		= "1"
			item['prod_code'] 		= site.xpath('ProductNo/text()').extract()
			item['prod_name'] 		= site.xpath('ProdName/text()').extract()
			item['prod_type']		= "1"
			item['start_amount']	= site.xpath('PurStarAmo/text()').extract()#PurStarAmo
			item['live_time']		= site.xpath('ProdLimit/text()').extract()#ProdLimit周期
			item['std_rate']		= site.xpath('ProdProfit/text()').extract()#ProdProfit利率
			item['risk_level']		= ""#风险等级
			item['create_time']		= time.time()#抓取时间
			item['total_type']		= "json"#全部数据类型：XML,JSON,HTML,ARRAY
			item['total_data']		= ""#全部数据
			
			#item['row'] = self.row
			#写入文件
			line = json.dumps(dict(item)) + '\n'
			self.file.write(line.decode("unicode_escape")) 
			self.row += 1
			#yield item
		self.page += 1
		urls = 'http://ewealth.abchina.com/app/data/api/DataService/BoeProductV2?i=%d&s=15&o=0&w=可售|||||||1||0||' %self.page
		
		try:
			if self.row < total:
				#print "正在读取...."
				yield scrapy.Request(urls, callback=self.parse)
		except:
			print "This Error"