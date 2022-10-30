import json
from select import select
from requests import request
import scrapy
from ..items import categoryStockMercedesItem, rrrGlobalStockItem
from scrapy.loader import ItemLoader


class categoryStockSpider(scrapy.Spider):
    name = 'rrrCategoryStock'
    allowed_domains = ['rrr.lt']
    start_urls = ['https://rrr.lt/lt/get_parts_ajax?q=mercedes']
    custom_settings = {'ITEM_PIPELINES': {'rrrScraper.pipelines.rrrCategoryStockPipeline': 400}}

    def parse(self, response):
        data = json.loads(response)
        # for categories in data['categories']['134']:
        #     yield request(categories['part_count'], callback=self)