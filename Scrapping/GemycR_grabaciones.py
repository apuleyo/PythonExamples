
# Librerías
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import date
from datetime import datetime
import time
import pandas as pd
import sys
import os

# Listas a utilizar para los datos
inicio=list()
duracion=list()
grabacion=list()
canal=list()
tipo_llamada=list()
participantes=list()

# Agregar el directorio del proyecto al sys.path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
project_dir = project_dir + r'\Scrapping'


"""
Return date in specific format to use in csv file name
 
Args:
    
Returns:
    string: The date in special format
 
Example:
    >>> horafecha()
    '27_11_2023-164332'
    """

# Funcion para sacar la hora y la fecha
def horafecha():
    now = datetime.now()
    format = now.strftime('%d_%m_%Y-%H%M%S')
    return format



# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--headless')              #Sin apertura del navegador

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = webdriver.ChromeOptions()
service = Service(r'C:\Users\luisangel.marugan\.wdm\drivers\chromedriver\win64\131.0.6778.85\chromedriver-win32\chromedriver.exe')  # Specify the path to your ChromeDriver
driver = webdriver.Chrome(service=service, options=options)


# Iniciarla en la pantalla 2
driver.set_window_position(2000, 0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador
driver.get('https://gemyc-r2.c2r.center.priv/gemycr-ui/#/login')

# Login
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                        "//input[contains(@autocomplete,'username')]")))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "//input[contains(@autocomplete,'username')]")))\
    .send_keys('administrador')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                        "//input[@type='password']")))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "//input[@type='password']")))\
    .send_keys('root123')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                        "//button[@type='submit'][contains(.,'Iniciar')]")))\
    .click()

# Accedemos a la página de grabaciones
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                        "(//span[contains(.,'Grabaciones')])[1]")))\
    .click()


WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                        "//button[@type='button'][contains(.,'Buscar')]")))\
    .click()



table=WebDriverWait(driver, 15)\
    .until(EC.presence_of_element_located((By.XPATH,
                                           ('//*[@id="recsTable"]/tbody'))))

# //*[@id="1968725"]/td[5]
# /html/body/div[1]/div/div[2]/div/section[2]/div[4]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[5]

time.sleep(25)

rows = table.find_elements(By.TAG_NAME, 'tr')
#participants =rows.find_elements(By.TAG_NAME,'i')

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    inicio.append(cells[0].text)
    duracion.append(cells[1].text)
    grabacion.append(cells[2].text)
    canal.append(cells[3].text)
    tipo_llamada.append(cells[4].text)
    participantes.append(cells[5].text)
    #for participant in participants:
        #participantes.append(cells[4].text)
    

df = pd.DataFrame({'Inicio': inicio, 'Duracion': duracion, 'Grabacion':grabacion, 'Canal': canal, 'Tipo llamada' : tipo_llamada, 'Participantes': participantes})
#df = pd.DataFrame({'Inicio': inicio, 'Duracion': duracion, 'Grabacion':grabacion, 'Canal': canal, 'Tipo llamada' : tipo_llamada})
print(df)
df.to_excel(project_dir+ r'\Grabaciones' +'_'+horafecha()+'.xlsx', index=False)


driver.quit()

