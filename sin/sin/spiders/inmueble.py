from typing import Any
import scrapy
from scrapy.http import Response
import re

class InmuebleSpider(scrapy.Spider):
    name = "inmueble"
    allowed_domains = ["www.fincaraiz.com.co"]
    #start_urls = ["https://fincaraiz.com.co/inmueble/lote-en-venta/bogota/bogota/10313139", "https://www.fincaraiz.com.co/inmueble/apartamento-en-venta/bella-suiza/bogota/10483815"]


    custom_settings = {
        'FEEDS': {
            'data_csv/%(name)s_%(time)s.csv': {
                'format': 'csv',
            },
            'data_json/%(name)s_%(time)s.json': {
                'format': 'json',
            }
        }
    }
    
    def start_requests(self):
        urls = [
            "https://fincaraiz.com.co/inmueble/lote-en-venta/bogota/bogota/10313139", 
            "https://www.fincaraiz.com.co/inmueble/apartamento-en-venta/bella-suiza/bogota/10483815"
        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)#, cookies=self.settings.get('COOKIES')
    
    def parse(self, response):
            image_url=response.css("div.jss224 img::attr(src)").get()
            ubicacion = response.css('p.jss65.jss73.jss166::text').get("")
            ubicacion_asociada=response.css('p.jss65.jss73.jss196.jss126::text').get("")
            descripcion=response.css('p.jss65.jss73.jss290.jss265::text').get("")
            img_ubicacion = response.css('#location img::attr(src)').get()
            url_parts = response.url.split('/')
            codigo_fr = url_parts[-1]

            
            #categories = response.css('.MuiBox-root.jss331.jss329')
            #for category in categories:
            #    category_name = category.css('.jss65.jss74::text').get()
            #    category_value = category.css('.jss65.jss74.jss.*.jss.*::text').get()


            # tabla donde están las descripciones: 'div.MuiBox-root.jss330.jss328'
            descripciones = {}
            x=response.css("div.MuiBox-root.jss330.jss328 p::text").getall()
            caract = [valor for valor in x if valor != 'al anunciante']
            for i in range(0, len(caract), 2):
                variable = caract[i].strip()  # Eliminar espacios en blanco alrededor del nombre
                valor = caract[i + 1].strip()  # Eliminar espacios en blanco alrededor del valor
                descripciones[variable]=valor
                 
            

            precio_scrapeado = response.css('div.jss10 p:nth-child(2)::text').get()
            #cadena_especifica = "$&nbsp;" #$\xa0
            #otra='$\xa0'
            # Aplicar expresión regular para extraer el valor numérico
            #x = re.search(f'{re.escape(cadena_especifica)}\s*([\d.,]+)', precio_scrapeado)
            #match = re.search(f'{re.escape(otra)}\s*([\d.,]+)', x)

            # Verificar si se encontró el valor numérico
            #if match:
             #   precio = match.group(1)
                # Limpiar el formato del precio (eliminar puntos y comas)
             #   precio = precio.replace('.', '').replace(',', '')

            
            #img_ubicacion ->id=location
            caracteristicas={}
            papa = response.css('#characteristics p::text').getall()
            for pollito in papa:
                 if pollito != "Características":
                    caracteristicas[pollito]=1# se coloca 1 en cada uno para confirmar su existencia :)
            
            #id=characteristics
            result= {
                "ubicacion": ubicacion,
                "ubicacion_asociada":ubicacion_asociada,
                "img_ubicacion":img_ubicacion,
                "codigo_fr":codigo_fr,
                #"precio(COP)": precio,
                "images": image_url,
                "descripcion":descripcion,
                "precio(COP)":precio_scrapeado
                
            }
            result.update(descripciones)
            result.update(caracteristicas)
            #print(result)
            yield result