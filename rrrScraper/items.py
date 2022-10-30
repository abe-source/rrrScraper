import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(text):
    return ''.join(text.split())

class rrrGlobalStockItem(scrapy.Item):
    audi = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    alfaRomeo = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    bmw = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    chevrolet = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())   
    chrysler = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())    
    citroen = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())   
    dacia = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())   
    ford = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())  
    fiat = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())  
    honda = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())  
    hyundai = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    infiniti = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    jaguar = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    kia = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    landRover = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    lexus = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    mercedesBenz = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    mazda = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    mitsubishi = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    nissan = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    opel = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    peugeot = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    renault = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    saab = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    subaru = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    suzuki = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    seat = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    skoda = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    toyota = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    volvo = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    vw = scrapy.Field(input_processor=MapCompose(remove_tags,remove_whitespace),
                        output_processor=TakeFirst())
    timeStamp = scrapy.Field(output_processor=TakeFirst())
    pass

class categoryStockMercedesItem(scrapy.Item):
    apsvietimo_sistema = scrapy.Field(output_processor=TakeFirst())
    degalu_misinio_sistema = scrapy.Field(output_processor=TakeFirst())
    duju_ismetimo_sistema = scrapy.Field(output_processor=TakeFirst())
    durys = scrapy.Field(output_processor=TakeFirst())
    galine_asis = scrapy.Field(output_processor=TakeFirst())
    galines_isores_detales = scrapy.Field(output_processor=TakeFirst())
    kebulas_kebulo_dalys_kablys = scrapy.Field(output_processor=TakeFirst())
    kitos_detales = scrapy.Field(output_processor=TakeFirst())
    oro_kondicianavimo_sistema_radiatoriai = scrapy.Field(output_processor=TakeFirst())
    pavaru_deze_sankaba_transmisija = scrapy.Field(output_processor=TakeFirst())
    priekine_asis = scrapy.Field(output_processor=TakeFirst())
    priekines_isores_detales = scrapy.Field(output_processor=TakeFirst())
    prietaisai_jungikliai_el_sistema = scrapy.Field(output_processor=TakeFirst())
    ratai_padangos_gaubtai = scrapy.Field(output_processor=TakeFirst())
    salonas_interjeras = scrapy.Field(output_processor=TakeFirst())
    stabdziu_sistema = scrapy.Field(output_processor=TakeFirst())
    stiklai = scrapy.Field(output_processor=TakeFirst())
    stiklu_apiplovimo_valymo_sistema = scrapy.Field(output_processor=TakeFirst())
    variklis = scrapy.Field(output_processor=TakeFirst())
    pass
