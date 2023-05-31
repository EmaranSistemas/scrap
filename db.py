import mysql.connector
import pandas as pd
import xlrd
cnx = mysql.connector.connect(
  host="209.45.83.59",
  user="sistemas",
  password="qbJITBTz29o8Svf",
  database="demo"
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

if __name__ == "__main__":
    file ='img.xls'
    print("fil <|>: ", file)
    df = pd.read_excel(file)
    a = xlrd.open_workbook(file)
    sheet = a.sheet_by_index(0)
    # print("sheet: ",sheet)
    sheet.cell_value(0, 0)

    for i in range(1, sheet.nrows):
        clase = sheet.cell_value(i, 0)
        idsubclase = sheet.cell_value(i, 1)
        subclase = sheet.cell_value(i, 2)
        subsubsub = sheet.cell_value(i, 3)
        cod = sheet.cell_value(i, 4)
        cod2 = sheet.cell_value(i, 5)
        cod3 = sheet.cell_value(i, 6)
        nobmre = sheet.cell_value(i, 7)
        print(cod,clase,subclase,cod2,nobmre)
        db = base_datos()
        #db.insertar(cod,clase,subclase,cod2,nobmre)




