# -*- coding: utf-8 -*-
import scrapy

from ..items import CultureFunder

class CulturalpromotionchSpider(scrapy.Spider):
    name = 'culturalpromotionch'
    allowed_domains = ['kulturförderung.ch', 'xn--kulturfrderung-1pb.ch']
    start_urls = ['http://kulturförderung.ch/en/search/?q=&select_area=new-media']
    # start_urls = ['http://kulturförderung.ch/en/address/600/']

    def parse(self, response):
        for url in response.css('#search-results .ct-item-content .ct-article-head header a::attr("href")').re('.*/address/.*'):
            yield scrapy.Request(response.urljoin(url), callback=self.parse_cf)

    def parse_cf(self, response):
        cf = CultureFunder()
        cf['name'] = response.css('h1[itemprop="name"]::text').extract_first()
        if cf['name'] is not None: cf['name'] = cf['name'].strip()
        cf['subtitle'] = response.css('article > header:nth-child(1) > h2:nth-child(5)::text').extract_first()
        if cf['subtitle'] is not None: cf['subtitle'] = cf['subtitle'].strip()
        cf['category'] = response.css('article > section:nth-child(2) > p:nth-child(2)::text').extract_first()
        if cf['category'] is not None: cf['category'] = cf['category'].strip().replace('Categories: ', '')
        cf['regions'] = response.css('article > section:nth-child(2) > p:nth-child(3)::text').extract_first()
        if cf['regions'] is not None: cf['regions'] = cf['regions'].strip().replace('Regions: ', '')
        cf['purpose'] = response.css('article > section:nth-child(2) > p:nth-child(4)::text').extract_first()
        if cf['purpose'] is not None: cf['purpose'] = cf['purpose'].strip().replace('Purpose: ', '')
        cf['focus'] = response.css('article > section:nth-child(2) > p:nth-child(5)::text').extract_first()
        if cf['focus'] is not None: cf['focus']= cf['focus'].strip().replace('Promotion focuses: ', '')
        cf['criteria'] = response.css('article > section:nth-child(2) > p:nth-child(6)::text').extract_first()
        if cf['criteria'] is not None: cf['criteria'] = cf['criteria'].strip().replace('Exclusion criteria: ', '')
        cf['application'] = response.css('article > section:nth-child(2) > p:nth-child(7)::text').extract_first()
        if cf['application'] is not None: cf['application'] = cf['application'].strip().replace('Applications: ', '')
        cf['website'] = response.css('article > section:nth-child(3) > p:nth-child(2) > a:nth-child(2)::text').extract_first()
        cf['dataurl'] = response.url
        return cf
