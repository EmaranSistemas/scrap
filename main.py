from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import zipfile
import os
import time
import pandas as pd
import xlrd
import shutil

import mysql.connector
from datetime import datetime
import time

#from db import base_datos

cnx = mysql.connector.connect(
  host="209.45.83.59",
  user="sistemas",
  password="qbJITBTz29o8Svf",
  database="supermercados_sa"
)
cursor = cnx.cursor()

"""
INSERT INTO `indicadores_inv_local`(`id`, `cod_local`, `descripcion`, `stock_unidades`, `stock_costo`, `dias_stock`, `mix`, `quiebres`, `sin_venta`, `stock_negativo`, `fecha`, `cambio`, `dif_stock_unidades`, `dif_stock_costo`, `dif_dias_stock`, `dif_Mix`, `dif_Quiebres`, `dif_Sin_venta`, `dif_Stock_Negativo`, `nuevo_registro`) VALUES
 ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8],[value-9],[value-10],[value-11],
 [value-12],[value-13],[value-14],[value-15],[value-16],[value-17],[value-18],[value-19],[value-20])
"""
class base_datos:
    def __int__(self):
        self.tablas = ['detalle_inventario','indicadores_inv_local','informecobertura_mix']

    def detalle_inv(self,cod_spsa,cod_proveeedor,descripcion,um,marcas,total,locales,cd,mix,q):
        sql = "INSERT INTO `detalle_inventario`(`cod_spsa`, `cod_proveeedor`, `descripcion`, `um`, `marcas`, `total`, `locales`, `cd`, `mix`, `q`, `fecha`)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        fecha_actual = datetime.now()
        fecha_texto = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

        val = (cod_spsa,cod_proveeedor,descripcion,um,marcas,total,locales,cd,mix,q,fecha_texto)
        cursor.execute(sql, val)
        cnx.commit()

    def indicadores_inv(self,cod_local, descripcion,stock_unidades,stock_costo,dias_stock,mix,quiebres,sin_venta, stock_negativo, cambio, dif_stock_unidades,dif_stock_costo, dif_dias_stock,dif_Mix,dif_Quiebres,dif_Sin_venta,dif_Stock_Negativo,nuevo_registro):
        sql = "INSERT INTO `indicadores_inv_local`(`" \
              "cod_local`, `descripcion`, `stock_unidades`, `stock_costo`, `dias_stock`, `mix`, `quiebres`, `sin_venta`, `stock_negativo`, `fecha`, `cambio`, `dif_stock_unidades`, `dif_stock_costo`, `dif_dias_stock`, `dif_Mix`, `dif_Quiebres`, `dif_Sin_venta`, `dif_Stock_Negativo`, `nuevo_registro`) VALUES (" \
                "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        fecha_actual = datetime.now()
        fecha_texto = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

        val = (cod_local,descripcion,stock_unidades,stock_costo,dias_stock,mix,quiebres,sin_venta,stock_negativo,fecha_texto, cambio, dif_stock_unidades,dif_stock_costo, dif_dias_stock,dif_Mix,dif_Quiebres,dif_Sin_venta,dif_Stock_Negativo,nuevo_registro)
        cursor.execute(sql, val)
        cnx.commit()

    def informe_cob(self,cod_spsa,cod_proveeedor,descripcion_producto,marca,estado,catalogo_locales,cobertura):
        sql = "INSERT INTO `informe_cobertura_mix`(`cod_spsa`, `cod_proveeedor`, `descripcion_producto`, `marca`, `estado`, `catalogo_locales`, `cobertura`, `fecha`) VALUES (" \
                  "%s,%s,%s,%s,%s,%s,%s,%s)"
        # sq = (20325756,0,'BATAN-CULANTRO-FRESCO-X3SBS','UN','BATAN',11.740,11.560,180.00,759,21,'2023-05-03 15:30:00')
        # fecha = datetime.now()
        fecha_actual = datetime.now()
        fecha_texto = fecha_actual.strftime('%Y-%m-%d %H:%M:%S')

        val = (cod_spsa,cod_proveeedor,descripcion_producto,marca,estado,catalogo_locales,cobertura,fecha_texto)
        cursor.execute(sql, val)
        cnx.commit()

#sistemas@emaransac.com
#Sm~18jn57

class scrap:
    def __init__(self):

        self.s = Service('F:\\YERSON\\chromedriver.exe')
        self.ruta_descarga = "D:\\ScrapFiles\\"
        self.ruta_descarga_rm = "D:\\ScrapFiles\\LastWeek\\"
        """
        self.s = Service("/home/yerson/Downloads/chromedriver_linux64/chromedriver")
        self.ruta_descarga = "/home/yerson/Downloads/"
        """

        self.db = base_datos()

        self.file_name = ""
        self.count = 0

        chromeOptions = Options()
        chromeOptions.add_experimental_option("prefs", {
            "download.default_directory": "D:\\ScrapFiles\\",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        chromeOptions.add_argument("--headless")
        self.driver = webdriver.Chrome(service=self.s,options=chromeOptions)

        #self.opciones = webdriver.Chrome(service=self.s,options=chromeOptions)
        #self.servicio = Service(self.s)
        #self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def move_file(self,file, root):
        shutil.move(file, root)
    def reset_file_name(self):
        self.file_name = ""

    def eliminar_archivos_carpeta(self,carpeta):
        archivos = os.listdir(carpeta)
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta, archivo)
            if os.path.isfile(ruta_archivo):
                os.remove(ruta_archivo)

    def getFileName(self):
        print("{ >> Get file name << }")
        for archivo in os.listdir(self.ruta_descarga):
            if archivo.endswith(".zip"):
                self.file_name = os.path.splitext(archivo)[0]
                print("filename get: ",self.file_name)
                return self.file_name

    def getFileName_rm(self):
        #print("{ >> Get file name << }")
        for archivo in os.listdir(self.ruta_descarga_rm):
            if archivo.endswith(".xls"):
                self.file_name = os.path.splitext(archivo)[0]
                #print("filename get: ",self.file_name)
                return self.file_name

    def unsip(self):
        print("{ >> Unzip file << }")
        #print("este error: ",self.ruta_descarga+self.getFileName())
        print("Ruta descarga: ",self.ruta_descarga)
        print("Ruta nombre: ", self.getFileName())
        ruta = self.ruta_descarga + self.getFileName()+'.zip'
        with zipfile.ZipFile(str(ruta), 'r') as zip_ref:
            zip_ref.extractall(self.ruta_descarga)
        print("file unzip success!!!")

    def removFile(self):
        print("{ >> Remove file << }")
        os.remove(os.path.splitext(self.ruta_descarga+self.getFileName())[0]+'.zip')
        os.remove(self.ruta_descarga+self.file_name+'.xls')
        print("file removed")

    def print_name(self):
        print("{ >>  file && Remove<< }")
        self.unsip()
        #ruta = self.ruta_descarga+self.getFileName()
        ruta = "D:\\LastWeek\\" + self.getFileName()
        #ruta = ruta[:-4]
        file = ruta+'.xls'
        print("fil <|>: ",file)

    def exel_size(self,m, n):
        max = m
        min = n
        num = 1
        if (max < n):
            max = n
            num = 2
            min = m
        return max,min,num

    def file_df_remove(self):
        #"""
        print("{ >>  file && Remove<< }")
        #+++++++++++++++++++++++++++
        #  ARCHIVO NUEVO
        #+++++++++++++++++++++++++++
        self.unsip()
        ruta = "D:\\ScrapFiles\\" + self.getFileName()
        file = ruta+'.xls'
        #print("fil <|>: ",file)

        #+++++++++++++++++++++++++++
        # REUCPERAR ARCHIVO ANTIGUO
        #+++++++++++++++++++++++++++
        antiguo = "D:\\ScrapFiles\\LastWeek\\" + self.getFileName_rm()
        file_antiguo = antiguo + '.xls'

        #"""

        #a = xlrd.open_workbook('D:\\ScrapFiles\\IndicadoresLocales_31-05-2023_120016.xls')#file
        a = xlrd.open_workbook(file)  # file
        sheet1 = a.sheet_by_index(0)
        sheet1.cell_value(0, 0)

        #b = xlrd.open_workbook('D:\\ScrapFiles\\LastWeek\\IndicadoresLocales_31-05-2023_091221.xls')#file_antiguo
        b = xlrd.open_workbook(file_antiguo)
        sheet2 = b.sheet_by_index(0)
        sheet2.cell_value(0, 0)


        #++++++++++++++++++++++++******
        #  INSERTAR A LA BASE DE DATOS
        #******************************

        max,min,pos = self.exel_size(sheet1.nrows, sheet2.nrows)
        if self.count == 0:
            for i in range(1,max):
                nuevo,cambio, dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta, dif_Stock_Negativo = [0,0, 0, 0, 0, 0, 0, 0, 0]
                if(i < min):
                    n1, n2, n3, n4, n5, n6, n7, n8, n9 = [sheet1.cell_value(i, 0), sheet1.cell_value(i, 1),
                                                          sheet1.cell_value(i, 2), sheet1.cell_value(i, 3),
                                                          sheet1.cell_value(i, 4),
                                                          sheet1.cell_value(i, 5), sheet1.cell_value(i, 6),
                                                          sheet1.cell_value(i, 7), sheet1.cell_value(i, 8)]
                    s1, s2, s3, s4, s5, s6, s7, s8, s9 = [sheet2.cell_value(i, 0), sheet2.cell_value(i, 1),
                                                          sheet2.cell_value(i, 2), sheet2.cell_value(i, 3),
                                                          sheet2.cell_value(i, 4),
                                                          sheet2.cell_value(i, 5), sheet2.cell_value(i, 6),
                                                          sheet2.cell_value(i, 7), sheet2.cell_value(i, 8)]
                    if (s1 == n1 and s2 == n2 and s3 == n3 and s4 == n4 and s5 == n5 and s6 == n6 and s7 == n7 and s8 == n8 and s9 == n9):
                        cambio = 0
                        nuevo = 0
                        #print("INSERTAR1",i," -> ",s1, s2, s3, s4, s5, s6, s7, s8, s9," -> ",nuevo,cambio, dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta,dif_Stock_Negativo)
                        self.db.indicadores_inv(s1, s2, s3, s4, s5, s6, s7, s8, s9,cambio, dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta,dif_Stock_Negativo,nuevo)
                    else:
                        cambio = 1
                        if (s1 == n1):
                            dif_stock_unidades = n3 - s3
                            dif_stock_costo = n4 - s4
                            dif_dias_stock = n5 - s5
                            dif_Mix = n6 - s6
                            dif_Quiebres = n7 - s7
                            dif_Sin_venta = n8 - s8
                            dif_Stock_Negativo = n9 - s9

                            if (pos == 1):
                                nuevo = 0
                                #print("INSERTAR2", i, " -> ", n1, n2, n3, n4, n5, n6, n7, n8, n9, " -> ",nuevo, cambio,
                                #      dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                                #      dif_Sin_venta, dif_Stock_Negativo)
                                self.db.indicadores_inv(s1, s2, s3, s4, s5, s6, s7, s8, s9, cambio, dif_stock_unidades,
                                                        dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                                                        dif_Sin_venta, dif_Stock_Negativo, nuevo)
                            else:
                                nuevo = 0
                                #print("INSERTAR3", i, " -> ", s1, s2, s3, s4, s5, s6, s7, s8, s9, " -> ",nuevo, cambio,
                                #      dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                                #      dif_Sin_venta, dif_Stock_Negativo)
                                self.db.indicadores_inv(s1, s2, s3, s4, s5, s6, s7, s8, s9, cambio, dif_stock_unidades,
                                                        dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                                                        dif_Sin_venta, dif_Stock_Negativo, nuevo)
                        else:
                            cambio = 0
                            if(n1==s1):
                                print(n1,s1)
                                nuevo = 0
                            else:
                                nuevo = 1
                            #print("INSERTAR4", i, " -> ", n1, n2, n3, n4, n5, n6, n7, n8, n9, " -> ",nuevo, cambio,
                            #      dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                            #      dif_Sin_venta, dif_Stock_Negativo)
                            self.db.indicadores_inv(s1, s2, s3, s4, s5, s6, s7, s8, s9, cambio, dif_stock_unidades,
                                                    dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                                                    dif_Sin_venta, dif_Stock_Negativo, nuevo)

                else:
                    if(pos == 1):
                        nuevo = 1
                        n1, n2, n3, n4, n5, n6, n7, n8, n9 = [sheet1.cell_value(i, 0), sheet1.cell_value(i, 1),
                                                              sheet1.cell_value(i, 2), sheet1.cell_value(i, 3),
                                                              sheet1.cell_value(i, 4),
                                                              sheet1.cell_value(i, 5), sheet1.cell_value(i, 6),
                                                              sheet1.cell_value(i, 7), sheet1.cell_value(i, 8)]
                        #print("INSERTAR5", i, " -> ", n1, n2, n3, n4, n5, n6, n7, n8, n9, " -> ",nuevo, cambio,
                        #      dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                        #      dif_Sin_venta, dif_Stock_Negativo)
                        self.db.indicadores_inv(n1, n2, n3, n4, n5, n6, n7, n8, n9, cambio, dif_stock_unidades,
                                                dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta,
                                                dif_Stock_Negativo, nuevo)
                    else:
                         nuevo = 1
                         s1, s2, s3, s4, s5, s6, s7, s8, s9 = [sheet2.cell_value(i, 0), sheet2.cell_value(i, 1),
                                                              sheet2.cell_value(i, 2), sheet2.cell_value(i, 3),
                                                              sheet2.cell_value(i, 4),
                                                              sheet2.cell_value(i, 5), sheet2.cell_value(i, 6),
                                                              sheet2.cell_value(i, 7), sheet2.cell_value(i, 8)]
                         #print("INSERTAR6", i, " -> ", s1, s2, s3, s4, s5, s6, s7, s8, s9, " -> ",nuevo, cambio,
                         #      dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres,
                         #      dif_Sin_venta, dif_Stock_Negativo)
                         self.db.indicadores_inv(s1, s2, s3, s4, s5, s6, s7, s8, s9, cambio, dif_stock_unidades,dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta,dif_Stock_Negativo, nuevo)




            self.eliminar_archivos_carpeta(self.ruta_descarga_rm)
            self.move_file(file,self.getFileName())





        elif self.count == 1:
            for i in range(1, sheet1.nrows):
                cod_spsa = sheet1.cell_value(i, 0)
                cod_proveeedor = sheet1.cell_value(i, 1)
                descripcion = sheet1.cell_value(i, 2)
                um = sheet1.cell_value(i, 3)
                marcas = sheet1.cell_value(i, 4)
                total = sheet1.cell_value(i, 5)
                locales = sheet1.cell_value(i, 6)
                cd = sheet1.cell_value(i, 7)
                mix = sheet1.cell_value(i, 8)
                q = sheet1.cell_value(i, 8)

                # print(cod_spsa,cod_proveeedor,descripcion,um,marcas,total,locales,cd,mix,q)
                self.db.detalle_inv(cod_spsa, cod_proveeedor, descripcion, um, marcas, total, locales, cd, mix, q)
            print("insertado detalle_inv")

        elif self.count == 2:
            for i in range(1, sheet1.nrows):
                cod_spsa = sheet1.cell_value(i, 0)
                cod_proveeedor = sheet1.cell_value(i, 1)
                descripcion_producto = sheet1.cell_value(i, 2)
                marca = sheet1.cell_value(i, 3)
                estado = sheet1.cell_value(i, 4)
                catalogo_locales = sheet1.cell_value(i, 5)
                cobertura = sheet1.cell_value(i, 6)

                # print(cod_spsa,cod_proveeedor,descripcion_producto,marca,estado,catalogo_locales,cobertura)
                self.db.informe_cob(cod_spsa, cod_proveeedor, descripcion_producto, marca, estado, catalogo_locales,cobertura)
            print("insertado informe_cob")
        self.removFile()
        self.count += 1


    def login(self):
        self.driver.get('https://b2b.intercorpretail.pe')

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
        time.sleep(3)
        print("[ >> Login << ]")


    def abastecimiento(self):
        time.sleep(5)
        triangle = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]')
        self.action.click(triangle).perform()
        time.sleep(8)
        print("[ >> 1. Init << ]")

        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span[2]')
        self.action.click(abast).perform()
        print("[ >> 2. Abastecimiento.. << ]")
        time.sleep(15)

        detalle = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/span[1]/span')
        #/html/body/div[2]/div[2]/div/div/span[1]/span
        #//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span
        #
        self.action.move_to_element(detalle)
        self.action.click(detalle).perform()
        time.sleep(7)
        print("[ >> 3. Detalle Inv << ]")

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(6)
        print("[ >> 4. Generar informe << ]")

        descargar = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div')
        descargar.click()
        time.sleep(8)
        print("[ >> 5. Descargar <<]")

        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        exel.click()
        time.sleep(6)
        print("[ >> 6. Formato << ]")

        archivo = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        archivo.click()
        time.sleep(6)
        print("[ >> 7. Archivo .xls << ]")

        zip = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/a/span')
        zip.click()
        print("[ >> 8. Descarga .zip << ]")
        time.sleep(12)

    def detalleinv(self):
        triangle = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]')
        self.action.click(triangle).perform()
        time.sleep(1)
        print("[ >> 1. Init << ]")

        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span[2]')
        self.action.click(abast).perform()
        time.sleep(7)
        print("[ >> 2. Abastecimiento.. << ]")

        local = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/span[2]/span')
        self.action.move_to_element(local)
        self.action.click(local).perform()
        time.sleep(3)
        print("[ >> 3. Detalle Inv << ]")

        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(6)
        print("[ >> 4. Generar informe << ]")


        Descarga = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[1]/div')
        Descarga.click()
        time.sleep(9)
        print("[ >> 5. Descargar << ]")


        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/div[1]/div')
        exel.click()
        time.sleep(2)
        print("[ >> 6. Formato << ]")


        Exel  = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        Exel.click()
        print("[ >> 7. Archivo .xls << ]")
        time.sleep(2)


        Seleccionar = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        Seleccionar.click()
        time.sleep(6)
        print("[ >> 8. Seleccionar << ]")


                                                         #'//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]'
        #'v-slot v-align-center v-align-middle'
        zip = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]')
        zip.click()
        print("[ >> 9. Descarga .zip.. << ]")
        time.sleep(2)

    def informeCv(self):
        time.sleep(1)
        triangle = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]')
        self.action.click(triangle).perform()
        time.sleep(4)
        print("[ >> 1. Init << ]")

        abast = self.driver.find_element(By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]/span[2]')
        self.action.click(abast).perform()
        time.sleep(6)
        print("[ >> 2. Abastecimiento << ]")



        detalle = self.driver.find_element(By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/span[3]/span')
        self.action.move_to_element(detalle)
        self.action.click(detalle).perform()
        time.sleep(3)
        print("[ >> 3. Detalle Inv << ]")


        generar = self.driver.find_element(by=By.CLASS_NAME,value='v-button.v-widget.btn-filter-search.v-button-btn-filter-search')
        generar.click()
        time.sleep(8)
        print("[ >> 4. Generar informe << ]")


        Descarga = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div[3]/div/div[1]/div')
        Descarga.click()
        time.sleep(5)
        print("[ >> 5. Descargar << ]")


        exel = self.driver.find_element(by=By.XPATH,value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/div[1]/div')
        exel.click()
        time.sleep(5)
        print("[ >> 6. Formato << ]")


        Exel  = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div/div/span[2]/label')
        Exel.click()
        time.sleep(5)
        print("[ >> 7. Archivo .xls << ]")


        Seleccionar = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/div')
        Seleccionar.click()
        time.sleep(12)
        print("[ >> 8. Seleccionar << ]")


        zip = self.driver.find_element(by=By.XPATH,value= '//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]')
        zip.click()
        print("[ >> 9. Descarga .zip << ]")

        time.sleep(3)

    def init(self):
        """
        self.login()

        print("[ >> 1.Abastecimiento << ]")
        self.abastecimiento()
        self.file_df_remove()
        time.sleep(5)
        self.reset_file_name()
        """
        self.eliminar_archivos_carpeta(self.ruta_descarga_rm)
        ruta = "D:\\ScrapFiles\\" + self.getFileName()
        file = ruta+'.xls'
        self.move_file(file, self.ruta_descarga_rm)






if __name__ == '__main__':
    sc = scrap()
    sc.init()
    sc.driver.quit()


