import datetime
import json
from select import select
from requests import request
import scrapy
from ..items import categoryStockMercedesItem
from scrapy.loader import ItemLoader


class categoryStockSpider(scrapy.Spider):
    name = 'rrrCategoryStock'
    allowed_domains = ['pstmn.io']
    start_urls = ['https://851ea191-8b5f-4052-8e39-f38cf44e3373.mock.pstmn.io/lt/get_parts_ajax?q=mercedes']
    custom_settings = {'ITEM_PIPELINES': {'rrrScraper.pipelines.rrrCategoryStockPipeline': 400}}

    def parse(self, response):
        data = json.loads(response.body)
        il = ItemLoader(item=categoryStockMercedesItem(), selector=data)
        il.add_value('apsvietimo_sistema', data['categories']['134']['part_count'])
        il.add_value('degalu_misinio_sistema', data['categories']['281']['part_count'])
        il.add_value('duju_ismetimo_sistema', data['categories']['1168']['part_count'])
        il.add_value('durys', data['categories']['579']['part_count'])
        il.add_value('galine_asis', data['categories']['382']['part_count'])
        il.add_value('galines_isores_detales', data['categories']['541']['part_count'])
        il.add_value('kebulas_kebulo_dalys_kablys', data['categories']['624']['part_count'])
        il.add_value('kitos_detales', data['categories']['1249']['part_count'])
        il.add_value('oro_kondicianavimo_sistema_radiatoriai', data['categories']['197']['part_count'])
        il.add_value('pavaru_deze_sankaba_transmisija', data['categories']['416']['part_count'])
        il.add_value('priekine_asis', data['categories']['330']['part_count'])
        il.add_value('priekines_isores_detales', data['categories']['498']['part_count'])
        il.add_value('prietaisai_jungikliai_el_sistema', data['categories']['999']['part_count'])
        il.add_value('ratai_padangos_gaubtai', data['categories']['463']['part_count'])
        il.add_value('salonas_interjeras', data['categories']['806']['part_count'])
        il.add_value('stabdziu_sistema', data['categories']['1']['part_count'])
        il.add_value('stiklai', data['categories']['1189']['part_count'])
        il.add_value('stiklu_apiplovimo_valymo_sistema', data['categories']['98']['part_count'])
        il.add_value('variklis', data['categories']['250']['part_count'])
        il.add_value('timeStamp', datetime.datetime.now().isoformat())
        il.add_value('currentPage', response.request.url)
        yield il.load_item()

        next_page = "https://851ea191-8b5f-4052-8e39-f38cf44e3373.mock.pstmn.io/lt/get_parts_ajax?q=bmw"

        yield scrapy.Request(next_page, callback=self.parse)

 