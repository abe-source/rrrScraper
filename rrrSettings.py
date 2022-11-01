from urllib.parse import parse_qs, urlparse

categoryStockSpiderUrls = ['https://rrr.lt/lt/get_parts_ajax?q=mercedes',
                           'https://rrr.lt/lt/get_parts_ajax?q=bmw',
                           'https://rrr.lt/lt/get_parts_ajax?q=jaguar',
                           'https://rrr.lt/lt/get_parts_ajax?q=vw']

categoryStockUrlsCarMakes = []

def getTableName(carMake):
       return "categoryStock" + carMake

def getCarMakeFromUrl(url):
       parsed = urlparse(url)
       return parse_qs(parsed.query)['q'][0].title()

for i in categoryStockSpiderUrls:
       foo = getCarMakeFromUrl(i)
       categoryStockUrlsCarMakes.append(foo)