from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import re 
import time

# Configura el WebDriver

def dicc_links(url, keyword, page):
    service = Service(executable_path='C:/Users/neylp/OneDrive/Escritorio/Scrapeo/Scrapy/Finca_Raiz/mientras/in/sin/sin/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.headless = False  # Configúralo en True si no quieres ver la ventana del navegador
    driver = webdriver.Chrome(service=service, options=options)

    # Visita la página que contiene los elementos
    driver.get(url)

    tiempoEspera=0.2
    ult = """//*[@id="listingResult"]/div[3]/div/nav/ul/li[8]/button"""
    elemento = WebDriverWait(driver, tiempoEspera).until(
        EC.presence_of_element_located((By.XPATH, ult))
    )

    cant_total = int(elemento.text) if elemento.text.isdigit() else 0

    dic = {}

    for i in range(1, cant_total + 1):
        # Espera hasta que el contenedor de listado sea visible
        cont = WebDriverWait(driver, tiempoEspera).until(
            EC.presence_of_element_located((By.ID, "listingContainer"))
        )

        # Extrae los elementos del enlace
        elementos = cont.find_elements(By.XPATH, '//*[@id="listingContainer"]/div/article/a')
        href_values = [elemento.get_attribute('href') for elemento in elementos]

        # Almacena la lista de enlaces en el diccionario
        dic[f"Página {i}"] = href_values

        # Imprime la cantidad de enlaces en la página actual
        cant = len(href_values)
        print(f"\nSe encontraron: {cant} links en la página {i}")

        # Si no es la última página, hacer clic en el botón "Siguiente"
        if i < cant_total:
            siguiente_btn = driver.find_element(By.XPATH, '//*[@id="listingResult"]/div[3]/div/nav/ul/li[9]')
            siguiente_btn.click()
            # Espera un tiempo para asegurarse de que la página siguiente se cargue completamente
            time.sleep(1)

    
    driver.quit()

    return dic

