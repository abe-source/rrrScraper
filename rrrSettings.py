from urllib.parse import parse_qs, urlparse

categoryStockSpiderUrls = ['https://851ea191-8b5f-4052-8e39-f38cf44e3373.mock.pstmn.io/lt/get_parts_ajax?q=mercedes',
                           'https://851ea191-8b5f-4052-8e39-f38cf44e3373.mock.pstmn.io/lt/get_parts_ajax?q=bmw']

categoryStockUrlsCarMakes = []

def getTableName(carMake):
       return "categoryStock" + carMake

def getCarMakeFromUrl(url):
       parsed = urlparse(url)
       return parse_qs(parsed.query)['q'][0].title()

for i in categoryStockSpiderUrls:
       foo = getCarMakeFromUrl(i)
       categoryStockUrlsCarMakes.append(foo)