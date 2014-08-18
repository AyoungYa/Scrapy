# Scrapy settings for ebookSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ebookSpider'

DEPTH_PRIORITY = 1

SPIDER_MODULES = ['ebookSpider.spiders']
NEWSPIDER_MODULE = 'ebookSpider.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ebookSpider (+http://www.yourdomain.com)'
