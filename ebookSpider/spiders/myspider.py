#!/usr/bin/python
#! -*- coding: utf-8 -*-
"""
contents:spider of http://www.douluodalu.com.cn
author:Yang
date:2014-6-26
"""

from scrapy.spider import Spider
from scrapy.selector import Selector
from ebookSpider.items import *
from scrapy.http import Request
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class urlSpider(Spider):
	name = "urlSpider"
	allowed_domains = ["douluodalu.com.cn"]
	start_urls = [
			"http://www.douluodalu.com.cn"
			]

	def parse(self, response):

		sel = Selector(response)
		url_list = sel.xpath('//td/a[@rel]/@href').extract()
		content = []
		f1 = open('list2.dat', 'w')
		for i in url_list[::-1]:
			f1.write(i)
			req = Request(i, self.contentparse)
			content.append(req)
		f1.close()
		return content
#			req = Request(i, self.contentparse)
   #     contents = []
    #    for url in url_list:
	#		req = Request(url, self.contentParse)
	#		contents.append(req)


	def contentparse(self, response):

		sel = Selector(response)
		content = sel.xpath('//p[1]/text()').extract()
		title = sel.xpath('//div/h1/text()').extract()
		patitle = sel.xpath('//a[@rel="category tag"]/text()').extract()
		s = ''
		s += title[0]
		for i in content:
			s += i
		#s += content[0]
		s += '\r\n'
		s += ''
#		print s 

		f1 = open('ch1.dat', 'a')
		f2 = open('ch2.dat', 'a')
		f3 = open('ch3.dat', 'a')
		f4 = open('ch4.dat', 'a')
		if patitle[0] == '斗罗世界':
			f1.writelines(s)
			print 1
		elif patitle[0] == '第一魂环':
			f2.writelines(s)
			print 2
		elif patitle[0] == '怪物学院':
			f3.writelines(s)
			print 3
		elif patitle[0] == '史莱克七怪':
			f4.writelines(s)
			print 4
		print s
		s = ''
		f1.close()
		f2.close()
		f3.close()
		f4.close()
