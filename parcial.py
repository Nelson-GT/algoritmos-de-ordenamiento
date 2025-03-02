import json
from datetime import datetime

class Descarga:
    def __init__(self,url,tamano,fecha_inicio,estado):
        self.url = url
        self.tamano = tamano
        self.fecha_inicio = fecha_inicio
        self.estado = estado

class HistorialDescargas:
    def __init__(self):
        self.cola_descargas = []
        self.historial_completadas = []
        self.cargar_descargas_desde_json("descargas.json")

    def cargar_descargas_desde_json(self, archivo_json):
        self.cola_descargas = []
        self.historial_completadas = []
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for descarga_data in datos:
                descarga = Descarga(
                    url=descarga_data['url'],
                    tamano=descarga_data['tamano'],
                    fecha_inicio=descarga_data['fecha_inicio'],
                    estado=descarga_data['estado']
                )
                # Clasificar las descargas según su estado
                if descarga.estado == 'completada':
                    self.historial_completadas.append(descarga)
                else:
                    self.cola_descargas.append(descarga)
    
    def mostrar_descargas(self):
        print("\nDescargas en la cola (pendientes y en progreso):")
        print("URL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in self.cola_descargas:
            print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        
        print("\nDescargas completadas:")
        print("URL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in self.historial_completadas:
            print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        print("\n")