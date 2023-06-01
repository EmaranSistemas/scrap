import mysql.connector
import pandas as pd
import xlrd
cnx = mysql.connector.connect(
  host="209.45.83.59",
  user="sistemas",
  password="qbJITBTz29o8Svf",
  database="supermercados_sa"
)
cursor = cnx.cursor()


class base_datos:
    def __int__(self):
        self.nombre = ""
    def insertar(self,referencia,clase,subclase,cod2,nobmre):
        sql = "INSERT INTO `contanet`(`referencia`, `clase`, `subclase`, `cod2`, `nobmre`) VALUES (" \
              "%s,%s,%s,%s,%s)"
        val = (referencia,clase,subclase,cod2,nobmre)
        cursor.execute(sql, val)
        cnx.commit()
    def insertar_locales(self,cod_local,nombre_local,formato,tipo,direccion,ciudad,estado):
        sql = "INSERT INTO `locales`(`cod_local`, `nombre_local`, `formato`, `tipo`, `direccion`, `ciudad`, `estado`) VALUES (" \
              "%s,%s,%s,%s,%s,%s,%s)"
        val = (cod_local,nombre_local,formato,tipo,direccion,ciudad,estado)
        cursor.execute(sql, val)
        cnx.commit()

"""
INSERT INTO `locales`(`id`, `cod_local`, `nombre_local`, `formato`, `tipo`, `direccion`, `ciudad`, `estado`) VALUES ([value-1],[value-2],[value-3],[value-4],[value-5],[value-6],[value-7],[value-8])
"""

if __name__ == "__main__":
    file ='locales.xls'
    df = pd.read_excel(file)
    a = xlrd.open_workbook(file)
    sheet = a.sheet_by_index(0)
    # print("sheet: ",sheet)
    sheet.cell_value(0, 0)

    for i in range(1, sheet.nrows):
        s1 = sheet.cell_value(i, 0)
        s2 = sheet.cell_value(i, 2)
        s3 = sheet.cell_value(i, 3)
        s4 = sheet.cell_value(i, 4)
        s5 = sheet.cell_value(i, 5)
        s6 = sheet.cell_value(i, 6)
        s7 = sheet.cell_value(i, 7)
        #print(s1,s2,s3,s4,s5,s6,s7)
        db = base_datos()
        db.insertar_locales(s1,s2,s3,s4,s5,s6,s7)




