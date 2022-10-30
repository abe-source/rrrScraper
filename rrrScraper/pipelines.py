# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

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
    pass
