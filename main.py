from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import json
import os
 
def main():
    print("Iniciando el navegador...")
    url = input("Introduce la URL: ")

    service = Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")  # Para ejecutar en segundo plano el navegador
    option.add_argument("--window-size=1200,900")
   
    print("Iniciando el servicio...")
    driver=webdriver.Chrome(service=service, options=option)
    
    print("Visitando:", url)
    driver.get(url)
    time.sleep(5)  
 
    texto = driver.find_element("tag name", "body").text
    data={
        "Texto visible": texto,
        "URL actual": driver.current_url
    }
 
    archivo_json = "datos.json"
 
    if os.path.exists(archivo_json):
        with open(archivo_json, "r", encoding="utf-8") as file:
            try:
                contenido = json.load(file)
            except json.JSONDecodeError:
                contenido = []
    else:
        contenido = []
 
    contenido.append(data)
    with open(archivo_json, "w", encoding="utf-8") as file:
        json.dump(contenido, file, ensure_ascii=False, indent=4)
 
    print(json.dumps(data, indent=4, ensure_ascii=False))
 
 
    url_actual = driver.current_url
    print("URL actual\n",url_actual)
    time.sleep(30)
    driver.quit()
 
if __name__ == "__main__":
    main()
# Este script esta hecho Selenium para extraer texto de una página web y guardarlo en el archivo datos.json.