from select import select
import scrapy
from ..items import RrrGlobalItem
from scrapy.loader import ItemLoader
import datetime
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


class RrrglobalSpider(scrapy.Spider):
    name = 'rrrGlobal'
    allowed_domains = ['rrr.lt']
    start_urls = ['http://rrr.lt/']

    def parse(self, response):     
        il = ItemLoader(item=RrrGlobalItem(), selector=response)
        il.add_xpath('audi', "//a[contains(text(),'Audi')]/span")
        il.add_xpath('alfaRomeo', "//a[contains(text(),'Alfa Romeo')]/span")
        il.add_xpath('bmw', "//a[contains(text(),'BMW')]/span")
        il.add_xpath('chevrolet', "//a[contains(text(),'Chevrolet')]/span")
        il.add_xpath('chrysler', "//a[contains(text(),'Chrysler')]/span")
        il.add_xpath('citroen', "//a[contains(text(),'Citroen')]/span")
        il.add_xpath('dacia', "//a[contains(text(),'Dacia')]/span")
        il.add_xpath('ford', "//a[contains(text(),'Ford')]/span")
        il.add_xpath('fiat', "//a[contains(text(),'Fiat')]/span")
        il.add_xpath('honda', "//a[contains(text(),'Honda')]/span")
        il.add_xpath('hyundai', "//a[contains(text(),'Hyundai')]/span")
        il.add_xpath('infiniti', "//a[contains(text(),'Infiniti')]/span")
        il.add_xpath('jaguar', "//a[contains(text(),'Jaguar')]/span")
        il.add_xpath('kia', "//a[contains(text(),'KIA')]/span")
        il.add_xpath('landRover', "//a[contains(text(),'Land Rover')]/span")
        il.add_xpath('lexus', "//a[contains(text(),'Lexus')]/span")
        il.add_xpath('mercedesBenz', "//a[contains(text(),'Mercedes-Benz')]/span")
        il.add_xpath('mazda', "//a[contains(text(),'Mazda')]/span")
        il.add_xpath('mitsubishi', "//a[contains(text(),'Mitsubishi')]/span")
        il.add_xpath('nissan', "//a[contains(text(),'Nissan')]/span")
        il.add_xpath('opel', "//a[contains(text(),'Opel')]/span")
        il.add_xpath('peugeot', "//a[contains(text(),'Peugeot')]/span")
        il.add_xpath('renault', "//a[contains(text(),'Renault')]/span")
        il.add_xpath('saab', "//a[contains(text(),'Saab')]/span")
        il.add_xpath('subaru', "//a[contains(text(),'Subaru')]/span")
        il.add_xpath('suzuki', "//a[contains(text(),'Suzuki')]/span")
        il.add_xpath('seat', "//a[contains(text(),'Seat')]/span")
        il.add_xpath('skoda', "//a[contains(text(),'Skoda')]/span")
        il.add_xpath('toyota', "//a[contains(text(),'Toyota')]/span")
        il.add_xpath('volvo', "//a[contains(text(),'Volvo')]/span")
        il.add_xpath('vw', "//a[contains(text(),'Volkswagen')]/span")
        il.add_value('timeStamp', datetime.datetime.now().isoformat())
        yield il.load_item()

class categoryStockMercedes(scrapy.Spider):
    name = 'categoryStockMercedes'
    allowed_domains = ['rrr.lt']
    start_urls = ['https://rrr.lt/lt/get_parts_ajax?q=mercedes']

    def parse(self, response):
        print(response.body)
