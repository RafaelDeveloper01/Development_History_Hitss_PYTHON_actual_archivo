#librerias de chrome para selenium y algunas mas de ayuda
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#unaopcion_para_enviar_msj_al_Wsp_(no usada)
import pywhatkit
#control local
import keyword
import pyautogui as pa
#numero o valor aleatorio
import random
#retraso
import time
#libreria_tiempo y suma de tiempo a la hora actual
from datetime import datetime, timedelta
import pytz
import os
from selenium.common.exceptions import NoSuchElementException
import glob
import subprocess
import requests

############################################################################################################################
#### INSTANCIA PRINCIPAL DE CHROME ###
# Crear una instancia de ChromeOptions----------------------
options = Options()
# Agregar la ruta de la extensión a las opciones de Chrome--

options.add_argument("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_ACTULIZAR_BI\\CHROME_EXT_EXE\\chromedriver.exe")
# Abrir el navegador completo-------------------------------
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.accept_insecure_certs = True
# Inicializar el controlador de Chrome con las opciones-----
driver = webdriver.Chrome(options=options)
time.sleep(2)
############################################################################################################################
############################################################################################################################
############################################################################################################################

#Abrir reporteador
#driver.get("https://172.19.112.62/central_login/index.php?action=remoteAuthenticacion&service=http://172.19.112.62/generador/custom/Atu_Canvia?ticketID=nhc3Yn3KP4Bpn7uZxmAYizGdLBvwtAFw&apiKey=fukL8Cw5456D4YkL0009uI7iK1W17Nqoi&warning=Argument%202%20passed%20to%20Monolog\Logger::addInfo()%20must%20be%20an%20array,%20object%20given,%20called%20in%20/var/www/html/central_login/src/Controllers/AuthController.php%20on%20line%20186%20and%20defined")
#time.sleep(5)


# URL de la página web que contiene el botón
url_pagina = "link_de_la_pagina"
driver.get(url_pagina)
# Encuentra los campos de usuario y contraseña   
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Ingresa las credenciales y presiona "Enter"  
username_field.send_keys("user") 
password_field.send_keys("pass")
password_field.send_keys(Keys.RETURN)

time.sleep(80)
# Espera a que se complete el inicio de sesión
# Reemplaza 'by' y 'value' con los valores reales para identificar el elemento
element_to_click = driver.find_element(By.XPATH, '//*[@id="action-buttons"]/a')  # Cambia 'el_id_del_elemento' al ID del elemento
element_to_click.click()
time.sleep(80)
# Haz clic en el elemento para iniciar la descarga
                   
carpeta_destino = "ruta_directorio"  # Reemplaza con la ruta de tu carpeta de destino
 # Reemplaza con el nombre que desees
for archivo in os.listdir(carpeta_destino):
    ruta_archivo = os.path.join(carpeta_destino, archivo)
    try:
        if os.path.isfile(ruta_archivo):
            os.remove(ruta_archivo)
            print(f"Se ha eliminado {ruta_archivo}")
    except Exception as e:
        print(f"No se pudo eliminar {ruta_archivo}: {e}")

time.sleep(10)
descargas_chrome = "ruta_descarga"
lista_archivos = os.listdir(descargas_chrome)
archivos_csv = [archivo for archivo in lista_archivos if archivo.lower().endswith('.csv')]
archivos_csv.sort(key=lambda x: os.path.getmtime(os.path.join(descargas_chrome, x)))
nombre_archivo = archivos_csv[-1]
ruta_destino = os.path.join(carpeta_destino, nombre_archivo)
#
nombre_personalizado = "ARCHIVO_GENERICO.csv"
ruta_destino_personalizado = os.path.join(carpeta_destino, nombre_personalizado)

# Mueve el archivo a la carpeta de destino con el nombre personalizado
os.rename(os.path.join(descargas_chrome, nombre_archivo), ruta_destino_personalizado)
#
# Mueve el archivo a la carpeta de destino


# Espera un tiempo para que se complete la descarga del archivo
time.sleep(5)  # Puedes ajustar el tiempo de espera según sea necesario
driver.quit()