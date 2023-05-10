from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import zipfile
import os
import pandas as pd
import mysql.connector
import xlrd
#sistemas@emaransac.com
#Sm~18jn57



class scrap:
    def __init__(self):

        self.s = Service('D:\\YERSON\\chromedriver.exe')
        self.ruta_descarga = "D:\\Usuario\\Downloads\\"
        """
        self.s = Service("/home/yerson/Downloads/chromedriver_linux64/chromedriver")
        self.ruta_descarga = "/home/yerson/Downloads/"
        """
        self.file_name = ""

        chromeOptions = Options()
        chromeOptions.headless = False

        #self.op = webdriver.ChromeOptions()
        #self.op.headless = True
        #self.op.add_argument("--headless")
        #self.op.headless = True


        #self.op.add_argument('--no-sandbox')
        #self.op.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(service=self.s,options=chromeOptions)

        #self.opciones = webdriver.Chrome(service=self.s,options=chromeOptions)
        #self.servicio = Service(self.s)
        #self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

        self.cnx = mysql.connector.connect(
            host="209.45.83.59",
            user="sistemas",
            password="qbJITBTz29o8Svf",
            database="supermercados_sa"
        )
        self.cursor_ = self.cnx.cursor()

    def insertar(Ci, Np, Cb, St, Ps, Ub):
        sql = "INSERT INTO `plazavea`(`codigo_interno`, `nom_producto`, `codigo_barras`, `stock`, `presentacion`, `ubicacion`)" \
              " VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Ci, Np, Cb, St, Ps, Ub)

        self.cursor_.execute(sql, val)
        self.cnx.commit()
        #self.cursor.execute(sql, val)
        #self.cnx.commit()


    def getFileName(self):
        for archivo in os.listdir(self.ruta_descarga):
            if archivo.endswith(".zip"):
                self.file_name = os.path.splitext(archivo)[0]
                print("filename get: ",self.file_name)
                return archivo


    def unsip(self):
        with zipfile.ZipFile(self.ruta_descarga+self.getFileName(), 'r') as zip_ref:
            zip_ref.extractall(self.ruta_descarga)
        print("file unzip success!!!")

    def removFile(self):
        os.remove(os.path.splitext(self.ruta_descarga+self.getFileName())[0]+'.zip')
        os.remove(self.ruta_descarga+self.file_name+'.xls')

        print("file removed")
    def file_df(self):
        self.unsip()
        ruta = os.path.splitext(self.ruta_descarga+self.getFileName())[0]
        file = ruta+'.xls'
        print("fil >>: ",file)
        df = pd.read_excel(file)
        #++++++++++++++++++++++++******
        #  INSERTAR A LA BASE DE DATOS
        #******************************
        print(df)
        self.removFile()


    def login(self):
        self.driver.get('https://b2b.intercorpretail.pe')
        self.driver.maximize_window()
        #self.driver.minimize_window()
        dropdownbox = self.driver.find_elements(by=By.TAG_NAME, value='Option')
        i = 0;
        while i < len(dropdownbox):
            if dropdownbox[i].text == 'Supermercados Peruanos S.A.':
                dropdownbox[i].click()
                break
            i += 1
        Ingresar = self.driver.find_element(by=By.CLASS_NAME,value='btn.btn-primary.btn-sm')
        Ingresar.click()

        email = self.driver.find_element(by=By.NAME,value='username')
        email.send_keys("ventas@emaransac.com")
        time.sleep(1)
        contrasenia = self.driver.find_element(by=By.NAME,value='password')
        contrasenia.send_keys("VENTAS2023")
        login = self.driver.find_element(by=By.CLASS_NAME,value='pf-c-button.pf-m-primary.pf-m-block.btn-lg')
        login.click()
        time.sleep(5)
        print("----> login <----")

    def log(self):
        self.driver.get('https://b2b.intercorpretail.pe')
        self.driver.maximize_window()
        options = self.driver.find_element(by=By.XPATH,value='//*[@id="url"]')
        self.action.click(options).perform()
        time.sleep(3)
        print("options")

        dropdownbox = self.driver.find_elements(by=By.TAG_NAME, value='Option')
        i = 0;
        while i < len(dropdownbox):
            if dropdownbox[i].text == 'Supermercados Peruanos S.A.':
                dropdownbox[i].click()
                break
            i += 1

        Ingresar = self.driver.find_element(by=By.CLASS_NAME,value='btn.btn-primary.btn-sm')
        Ingresar.click()

        email = self.driver.find_element(by=By.NAME,value='username')
        email.send_keys("ventas@emaransac.com")
        time.sleep(1)
        contrasenia = self.driver.find_element(by=By.NAME,value='password')
        contrasenia.send_keys("VENTAS2023")
        login = self.driver.find_element(by=By.CLASS_NAME,value='pf-c-button.pf-m-primary.pf-m-block.btn-lg')
        login.click()
        time.sleep(443)
        print("----> login <----")


        abast = self.driver.find_element(By.XPATH, value='/html/body')
        self.action.click(abast).perform()
        time.sleep(1)
        print("abastecimiento")

        local = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span')
        self.action.move_to_element(local)
        self.action.click(local).perform()
        time.sleep(2)
        print("local")

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(4)
        print("generar")



    def abastecimiento(self):
        time.sleep(7)
        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]/span[2]')
        self.action.click(abast).perform()
        time.sleep(7)
        print("abastecimiento")

        local = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span')
        self.action.move_to_element(local)
        self.action.click(local).perform()
        time.sleep(6)
        print("local")

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(6)
        print("generar")

        descargar = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div')
        descargar.click()
        time.sleep(6)
        print("descargar")

        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        exel.click()
        time.sleep(6)
        print("exel")

        archivo = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        archivo.click()
        time.sleep(6)
        print("archivo")

        zip = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span')
        zip.click()
        print("zip")

        time.sleep(2)

    def detalleinv(self):
        time.sleep(2)
        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]/span[2]')
        self.action.click(abast).perform()
        time.sleep(2)
        detalle = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[2]/span')
        self.action.move_to_element(detalle)
        self.action.click(detalle).perform()
        time.sleep(5)

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(2)
        print("Generando reporte")

        Descarga = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[1]/div')
        Descarga.click()
        time.sleep(2)
        print("Descargando reporte")

        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/div[1]/div')
        exel.click()
        time.sleep(2)
        print("exel formato")

        Exel  = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        Exel.click()
        time.sleep(2)
        print("EXEL formato")

        Seleccionar = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        Seleccionar.click()
        time.sleep(7)
        print("Seleccionando archivo")

        zip = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]')
        zip.click()
        print("ZIP archivo")
        time.sleep(2)

    def informeCv(self):
        time.sleep(2)
        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]/span[2]')
        self.action.click(abast).perform()
        time.sleep(2)
        print("Abastecimiento")


        detalle = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[3]/span')
        self.action.move_to_element(detalle)
        self.action.click(detalle).perform()
        time.sleep(3)
        print("Detalle")

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(8)
        print("Generando reporte")

        Descarga = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div[3]/div/div[1]/div')
        Descarga.click()
        time.sleep(3)
        print("Descargando reporte")

        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/div[1]/div')
        exel.click()
        time.sleep(3)
        print("exel formato")

        Exel  = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        Exel.click()
        time.sleep(3)
        print("EXEL formato")

        Seleccionar = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        Seleccionar.click()
        time.sleep(6)
        print("Seleccionando archivo")

        zip = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]')
        zip.click()
        print("ZIP archivo")
        time.sleep(3)
    def upload(self):
        db.unsip()
        db.file_df()

    def init(self):
        self.login()
        print("Iniciando abastecimiento")
        self.abastecimiento()
        self.file_df()
        time.sleep(5)

        print("Iniciando detalle inventario")
        self.detalleinv()
        self.file_df()
        time.sleep(5)

        self.login()
        print("Iniciando informe cv")
        self.informeCv()
        self.file_df()
        print("--FIN--")


db = scrap()
#db.log()
db.init()
db.driver.quit()

sales
invoice_type_id
    tipo 3 --> note_cretito

2 tablas de notas de cretido


sales2

sales2_details

