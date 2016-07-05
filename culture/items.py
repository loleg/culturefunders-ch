# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class CultureFunder(Item):

	name = Field()
	subtitle = Field()
	category = Field()
	regions = Field()
	purpose = Field()
	focus = Field()
	criteria = Field()
	application = Field()
	website = Field()
	dataurl = Field()
