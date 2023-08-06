# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PostCodeItem(scrapy.Item):
   states = scrapy.Field()
   states_abbrv = scrapy.Field()
   city = scrapy.Field()
   district = scrapy.Field()
   postcode = scrapy.Field()

