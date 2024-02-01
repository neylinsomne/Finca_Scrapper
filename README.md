# Finca_Scrapper
Extracción de todos los inmuebles públicados en Finca Raiz para Bogotá mediante Scrappy. Específicamente solo los inmuebles en arriendo, si están interesados en también obtener aquellos con la etiqueta de "proyectos de vivienda" o con respecto a otra zona que no sea Bogotá se pueden comunicar conmigo :), o ustedes hacerlo cambiando este código. 





[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]([https://github.com/builker-col/bogota-apartments](https://github.com/neylinsomne))
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/neyl-peñuela-bernate-a76644209/)

[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/erik172/bogota-apartments)

La última fecha de scrapeo fue: **30 de Enero de 2024**

_Este proyecto hace parte [Linemeup]


## Cómo usarlo?
Primero para poder obtener todos los sub-links de las viviendas, debes conectarlo a la biblioteca SELENIUM y en el archivo "links.py", descargando un chromio. Aquí en este link puedes entender cómo
https://www.youtube.com/watch?v=NB8OceGZGjA&t=1s
ERROR 403?:
La página principal primero está cargada dinámicamente asi que Scrappy no va a poder hacerlo por su cuenta, puedes hacerlo con pyppeteer, pero con esto es más facíl hacerlo con Selenium a mi parecer.
De igual manera tendrás que conectar una función nueva que conecte los links extraidos de la página principal de Finca Raiz.

## ¿Por qué no pasar el código completo?
Esto es para que más gente pueda tener una plantilla base y lo puedan acomodar a su interes, y obviamente puedan hacerlo de una manera más optima. Al igual estaré cargando rutinarimente archivos json y csv que necesitan manejo.
