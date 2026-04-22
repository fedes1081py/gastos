from pathlib import Path
from datetime import datetime
import csv


ruta_historial = Path(__file__).absolute().parent / 'historial.csv'

class Historial:
    def __init__(self,ruta_historial):
        self.ruta_historial = ruta_historial

    def cargar_historial(self):
        if not self.ruta_historial.exist():
            return []
        with open(self.ruta_historial,'r',encoding='utf-8') as file:
            return list(csv.DictReader(file))

    def agregar_historial(self,diccionario):
        existe_ruta = self.ruta_historial.exist()

        with open(self.ruta_historial,'a',newline="",encoding='utf-8') as file:
            campos = ['id','descripcion','importe','prioridad','categoria']
            append = csv.DictWriter(file,fieldnames=campos)
            if not existe_ruta:
                append.writeheader()

            append.writerow(diccionario)


class Gasto:
    def __init__(self,descripcion, importe,prioridad,categoria,fecha):
        self.descripcion = descripcion
        self.importe = importe
        self.prioridad = prioridad 
        self.categoria = categoria
        self.fecha = fecha

    @property
    def importe(self):
        return self._importe
    @importe.setter
    def importe(self,importe):
        if importe < 0:
            return
        self._importe = importe

    @property
    def fecha(self):
        return self._fecha
    @fecha.setter
    def fecha(self,fecha):
        fecha_parseada = datetime.strftime(fecha,)


    





