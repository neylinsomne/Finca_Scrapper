# Finca_Scrapper
Extracción de todos los inmuebles públicados en Finca Raiz para Bogotá . Específicamente solo los inmuebles, si están interesados en también obtener aquellos con la etiqueta de "proyectos de vivienda" o con respecto a otra zona que no sea Bogotá se pueden comunicar conmigo :)





[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]([https://github.com/builker-col/bogota-apartments](https://github.com/neylinsomne))
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/neyl-peñuela-bernate-a76644209/)

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/erik172/bogota-apartments)

La última fecha de scrapeo fue: **30 de Enero de 2024**


## Índice
- [Bogota Apartments](#bogota-apartments)
  - [Data Source](#data-source)
  - [Datos](#datos)




## Descripción

El Proyecto Bogotá Apartments es una iniciativa de código abierto que busca recopilar y analizar datos sobre el mercado inmobiliario de apartamentos en la ciudad de Bogotá, Colombia. Utilizando avanzadas técnicas de web scraping y análisis de datos, este proyecto recopila información detallada sobre las ventas y alquileres de apartamentos en la ciudad, incluyendo un histórico de precios que brinda una visión temporal de la evolución del mercado.

El conjunto de datos generado está disponible para cualquier persona interesada en conocer más sobre el mercado inmobiliario de Bogotá y sus tendencias. Además, el proyecto presenta un análisis exploratorio de datos minucioso que proporciona información valiosa acerca de los precios, ubicaciones y características de los apartamentos en la ciudad.

El propósito fundamental del proyecto es estimular la investigación y el aprendizaje en el ámbito del análisis de datos y la ciencia de datos. El conjunto de datos puede ser utilizado para entrenar modelos de aprendizaje automático y realizar análisis más profundos sobre el mercado inmobiliario de la ciudad.

_Este proyecto hace parte [Builker](https://github.com/Builker-col)._




| Columna                              | Descripción                                               |
|--------------------------------------|-----------------------------------------------------------|
| codigo                               | Código único que identifica cada apartamento              |
| tipo_propiedad                       | Tipo de propiedad (apartamento, casa, etc.)               |
| tipo_operacion                       | Tipo de operación (venta, arriendo, etc.)                 |
| precio_venta                         | Precio de venta del apartamento COP                       |
| precio_arriendo                      | Precio de arriendo del apartamento COP                    |
| area                                 | Área del apartamento en metros cuadrados                  |
| habitaciones                         | Número de habitaciones del apartamento                    |
| banos                                | Número de baños del apartamento                           |
| administracion                       | Valor de la cuota de administración del apartamento       |
| parqueaderos                         | Número de parqueaderos disponibles                        |
| sector                               | Sector o zona en la que se encuentra el apartamento       |
| estrato                              | Estrato socioeconómico del apartamento                    |
| antiguedad                           | Antigüedad del apartamento en años                        |
| estado                               | Estado del apartamento (nuevo, usado)                     |
| longitud                             | Longitud geográfica del apartamento                       |
| latitud                              | Latitud geográfica del apartamento                        |
| descripcion                          | Descripción detallada del apartamento                     |
| datetime                             | Fecha y hora de extracción de los datos                   |
| jacuzzi                              | Indica si el apartamento cuenta con jacuzzi               |
| piscina                              | Indica si el apartamento cuenta con piscina               |
| salon_comunal                        | Indica si el apartamento cuenta con salón comunal         |
| terraza                              | Indica si el apartamento cuenta con terraza               |
| vigilancia                           | Indica si el apartamento cuenta con vigilancia privada    |
| piso                                 | Número de piso en el que se encuentra el apartamento      |
| closets                              | Número de closets en el apartamento                       |
| chimenea                             | Indica si el apartamento cuenta con chimenea              |
| permite_mascotas                     | Indica si se permiten mascotas en el apartamento          |
| gimnasio                             | Indica si el apartamento cuenta con gimnasio              |
| ascensor                             | Indica si el edificio cuenta con ascensor                 |
| conjunto_cerrado                     | Indica si el apartamento se encuentra en conjunto cerrado |
| coords_modified                      | Coordenadas modificadas del apartamento                   |
| localidad                            | Localidad en la que se encuentra el apartamento           |
| barrio                               | Barrio en el que se encuentra el apartamento              |
| estacion_tm_cercana                  | Nombre de la estacion de transporte masivo mas cercana    |
| distancia_estacion_tm_m              | Distancia a la estación de transporte masivo más cercana  |
| is_cerca_estacion_tm                 | Indica si está cerca de una estación de transporte masivo <= 500m |
| parque_cercano                       | Nombre del parque más cercano al apartamento              |
| distancia_parque_m                   | Distancia al parque más cercano al apartamento en metros  |
| is_cerca_parque                      | Indica si está cerca de un parque <= 500m                  |
| website                              | Sitio web relacionado a la propiedad                      |
| compañia                             | Compañía o agencia responsable de la propiedad            |
| last_view                            | Fecha de la ultima vez que el scraper visito el apartamento |
| timeline                             | Historial de precios del apartamento                      |
| url                                  | URL del apartamento                                       |

