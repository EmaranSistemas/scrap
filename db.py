import mysql.connector
from datetime import datetime
import time

cnx = mysql.connector.connect(
  host="209.45.83.59",
  user="sistemas",
  password="qbJITBTz29o8Svf",
  database="supermercados_sa"
)
cursor = cnx.cursor()


class base_datos:
    def __int__(self):
        self.tablas = ['detalle_inventario','indicadores_inv_local','informecobertura_mix']

    def insertar(self,cod_spsa,cod_proveeedor,descripcion,um,marcas,total,locales,cd,mix,q):
        sql = "INSERT INTO `detalle_inventario`(`cod_spsa`, `cod_proveeedor`, `descripcion`, `um`, `marcas`, `total`, `locales`, `cd`, `mix`, `q`, `fecha`) VALUES (" \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #sq = (20325756,0,'BATAN-CULANTRO-FRESCO-X3SBS','UN','BATAN',11.740,11.560,180.00,759,21,'2023-05-03 15:30:00')
        #fecha = datetime.now()
        fecha_str = '2023-05-03 15:30:00'
        fecha_datetime = datetime(*(time.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')[0:6]))

        val = (cod_spsa,cod_proveeedor,descripcion,um,marcas,total,locales,cd,mix,q,fecha_datetime)
        cursor.execute(sql, val)
        cnx.commit()

if __name__ == "__main__":
    db = base_datos()
    db.insertar(30325756,0,'BATAN-CULANTRO-FRESCO-X3SBS','UN','BATAN',11.740,11.560,180.00,759,21)




"""
for i in range(num_df):
    print("++++++++\n")
    Ci = data.loc[i, 'Codigo interno']
    Np = data.loc[i, 'Nombre del producto']
    Cb = data.loc[i, 'Código de barras']
    St = data.loc[i, 'Stock  (Wilkins80)']
    Ps = data.loc[i, 'Presentación']
    Ub = data.loc[i, 'Ubicación predeterminada']
    print(Ci, Np, Cb, St, Ps, Ub)
    insertar(Ci, Np, Cb, St, Ps, Ub)
"""