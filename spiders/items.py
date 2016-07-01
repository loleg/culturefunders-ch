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
	url = Field()
