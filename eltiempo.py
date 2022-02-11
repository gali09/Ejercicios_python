from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# opciones de Chrome
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')
option.add_argument('--disable-extensions')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)

# Inicializar Chrome
driver.get('https://www.eltiempo.es/')

cookie = WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button' \
                                       .replace(' ', '.'))))
cookie.click()

eltiempoen = WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'input#term')))
eltiempoen.send_keys('Torre del campo')
time.sleep(5)
eltiempoen.send_keys(Keys.ENTER)


WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[5]/main/div[4]/div/section[2]/section/div/ul/li/a')))\
    .click()

por_horas = WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[5]/main/div[4]/div/section[5]/section/div/article/section[1]/ul/li[2]/h2/a')))
por_horas.send_keys(Keys.ENTER)


WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')))

texto_columnas = driver.find_element_by_xpath('/html/body/div[5]/main/div[4]/div/section[5]/section/div[1]/ul')
texto_columnas = texto_columnas.text

tiempo_hoy = texto_columnas.split('Mañana')[0].split('\n')[1:-1]

horas= list()
temp= list()
viento = list()

for i in range(0,len(tiempo_hoy),4):
    horas.append(tiempo_hoy[i])
    temp.append(tiempo_hoy[i+1])
    viento.append(tiempo_hoy[i+2])

df= pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Viento(km/h)': viento})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()