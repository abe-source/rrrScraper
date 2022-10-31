# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import urllib
from urllib.parse import parse_qs, urlparse

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# https://github.com/RockyZ/Scrapy-sqlite-item-exporter/blob/master/exporters.py

class rrrGlobalStockPipeline:
    
    def __init__(self):
        self.con = sqlite3.connect('rrrGlobalStock.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):  
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS globalStock(
            timeStamp TEXT PRIMARY KEY,
            audi INTEGER,
            alfaRomeo INTEGER,
            bmw INTEGER,
            chevrolet INTEGER,
            chrysler INTEGER,
            citroen INTEGER,
            dacia INTEGER,
            ford INTEGER,
            fiat INTEGER,
            honda INTEGER,
            hyundai INTEGER,
            infiniti INTEGER,
            jaguar INTEGER,
            kia INTEGER,
            landRover INTEGER,
            lexus INTEGER,
            mercedesBenz INTEGER,
            mazda INTEGER,
            mitsubish INTEGER,
            nissan INTEGER,
            opel INTEGER,
            peugeot INTEGER,
            renault INTEGER,
            saab INTEGER,
            subaru INTEGER,
            suzuki INTEGER,
            seat INTEGER,
            skoda INTEGER,
            toyota INTEGER,
            volvo INTEGER,
            vw INTEGER
        )
        """)
    
    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO globalStock VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (item['timeStamp'],
                         item['audi'],
                         item['alfaRomeo'],
                         item['bmw'],
                         item['chevrolet'],
                         item['chrysler'],
                         item['citroen'],
                         item['dacia'],
                         item['ford'],
                         item['fiat'],
                         item['honda'],
                         item['hyundai'],
                         item['infiniti'],
                         item['jaguar'],
                         item['kia'],
                         item['landRover'],
                         item['lexus'],
                         item['mercedesBenz'],
                         item['mazda'],
                         item['mitsubishi'],
                         item['nissan'],
                         item['opel'],
                         item['peugeot'],
                         item['renault'],
                         item['saab'],
                         item['subaru'],
                         item['suzuki'],
                         item['seat'],
                         item['skoda'],
                         item['toyota'],
                         item['volvo'],
                         item['vw'],))
        self.con.commit()
        return item

class rrrCategoryStockPipeline:
    
    def __init__(self):
        self.con = sqlite3.connect('rrrGlobalStock.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        carMakeListForDb = ['Mercedes', 'Bmw']
        for i in carMakeListForDb:
            self.cur.execute('''
            CREATE TABLE IF NOT EXISTS {}(
                timeStamp TEXT PRIMARY KEY,
                apsvietimo_sistema INTEGER,
                degalu_misinio_sistema INTEGER,
                duju_ismetimo_sistema INTEGER,
                durys INTEGER,
                galine_asis INTEGER,
                galines_isores_detales INTEGER,
                kebulas_kebulo_dalys_kablys INTEGER,
                kitos_detales INTEGER,
                oro_kondicianavimo_sistema_radiatoriai INTEGER,
                pavaru_deze_sankaba_transmisija INTEGER,
                priekine_asis INTEGER,
                priekines_isores_detales INTEGER,
                prietaisai_jungikliai_el_sistema INTEGER,
                ratai_padangos_gaubtai INTEGER,
                salonas_interjeras INTEGER,
                stabdziu_sistema INTEGER,
                stiklai INTEGER,
                stiklu_apiplovimo_valymo_sistema INTEGER,
                variklis INTEGER
            )
            '''.format("categoryStock" + i))
    
    def process_item(self, item, spider):
        parsed = urlparse(item['currentPage'])
        carMake = parse_qs(parsed.query)['q'][0].title()
        tableName = "categoryStock" + carMake
        self.cur.execute('''INSERT OR IGNORE INTO {} VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''.format(tableName),
                        (item['timeStamp'],
                         item['apsvietimo_sistema'],
                         item['degalu_misinio_sistema'],
                         item['duju_ismetimo_sistema'],
                         item['durys'],
                         item['galine_asis'],
                         item['galines_isores_detales'],
                         item['kebulas_kebulo_dalys_kablys'],
                         item['kitos_detales'],
                         item['oro_kondicianavimo_sistema_radiatoriai'],
                         item['pavaru_deze_sankaba_transmisija'],
                         item['priekine_asis'],
                         item['priekines_isores_detales'],
                         item['prietaisai_jungikliai_el_sistema'],
                         item['ratai_padangos_gaubtai'],
                         item['salonas_interjeras'],
                         item['stabdziu_sistema'],
                         item['stiklai'],
                         item['stiklu_apiplovimo_valymo_sistema'],
                         item['variklis'],))
        self.con.commit()
        return item

class rrrCategoryStockPipeline2:
    pass
