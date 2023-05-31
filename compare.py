import mysql.connector
import pandas as pd
import xlrd
import shutil
import os

def move_file(file,root):
    shutil.move(file, root)

def exel_size(m,n):
    max = m
    num = 1
    if(max<n):
        max = n
        num = 2
    return max,num




def compare_files(file1,file2):
    a = xlrd.open_workbook(file1)
    b = xlrd.open_workbook(file2)
    sheet1 = a.sheet_by_index(0)
    sheet2 = b.sheet_by_index(0)
    sheet1.cell_value(0, 0)
    sheet2.cell_value(0, 0)


    for i in range(1, exel_size(sheet1.nrows,sheet2.nrows)):
        s1,s2,s3,s4,s5,s6,s7,s8,s9 = [sheet1.cell_value(i, 0),sheet1.cell_value(i, 1),sheet1.cell_value(i, 2),
                                      sheet1.cell_value(i, 3),sheet1.cell_value(i, 4),sheet1.cell_value(i, 5),
                                      sheet1.cell_value(i, 6),sheet1.cell_value(i, 7),sheet1.cell_value(i, 8)]

        n1,n2,n3,n4,n5,n6,n7,n8,n9 = [sheet2.cell_value(i, 0),sheet2.cell_value(i, 1),sheet2.cell_value(i, 2),
                                      sheet2.cell_value(i, 3),sheet2.cell_value(i, 4),sheet2.cell_value(i, 5),
                                      sheet2.cell_value(i, 6),sheet2.cell_value(i, 7),sheet2.cell_value(i, 8)]

        #print(s1,s2,s3,s4,s5,s6,s7,s8)
        cambio,dif_stock_unidades,dif_stock_costo,dif_dias_stock,dif_Mix,dif_Quiebres,dif_Sin_venta,dif_Stock_Negativo = [0,0,0,0,0,0,0,0]
        if(s1==n1 and s2==n2 and s3==n3 and s4==n4 and s5==n5 and s6==n6 and s7==n7 and s8==n8 and s9==n9):
            cambio = 0
            print(cambio, dif_stock_unidades, dif_stock_costo, dif_dias_stock, dif_Mix, dif_Quiebres, dif_Sin_venta,
                  dif_Stock_Negativo)
        else:
            cambio = 1
            if(s1==n1):
                dif_stock_unidades = n3-s3
                dif_stock_costo = n4-s4
                dif_dias_stock = n5-s5
                dif_Mix = n6-s6
                dif_Quiebres = n7-s7
                dif_Sin_venta = n8-s8
                dif_Stock_Negativo = n9-s9
        print(cambio,dif_stock_unidades,dif_stock_costo,dif_dias_stock,dif_Mix,dif_Quiebres,dif_Sin_venta,dif_Stock_Negativo)





if __name__ == "__main__":
   num,pos = exel_size(33,444)
   print(num)
   print(pos)