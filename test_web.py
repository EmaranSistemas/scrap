from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_argument("--headless") # asegura que el navegador se ejecute en modo headless
options.add_argument("--no-sandbox") # desactiva el modo sandbox
options.binary_location = '/usr/bin/chromium-browser'
# asegúrate de que el webdriver esté en tu PATH
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

driver.get('https://b2b.intercorpretail.pe')

dropdownbox = driver.find_elements(by=By.TAG_NAME, value='Option')
i = 0
while i < len(dropdownbox):
    if dropdownbox[i].text == 'Supermercados Peruanos S.A.':
        dropdownbox[i].click()
        break
    i += 1
Ingresar = driver.find_element(by=By.CLASS_NAME,value='btn.btn-primary.btn-sm')
Ingresar.click()

email = driver.find_element(by=By.NAME,value='username')
email.send_keys("ventas@emaransac.com")
time.sleep(1)
contrasenia = driver.find_element(by=By.NAME,value='password')
contrasenia.send_keys("VENTAS2023")
login = driver.find_element(by=By.CLASS_NAME,value='pf-c-button.pf-m-primary.pf-m-block.btn-lg')
login.click()
time.sleep(3)
print("[ >> Login << ]")

time.sleep(5)
triangle = driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]')
action.click(triangle).perform()
time.sleep(1)
print("[ >> 1. Init << ]")

abast = driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span[2]')
action.click(abast).perform()
print("[ >> 2. Abastecimiento.. << ]")
time.sleep(15)

detalle = driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/span[1]/span')
action.move_to_element(detalle)
action.click(detalle).perform()
time.sleep(3)
print("[ >> 3. Detalle Inv << ]")

generar = driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
generar.click()
time.sleep(6)
print("[ >> 4. Generar informe << ]")

# tu código de scraping va aquí

driver.quit()
