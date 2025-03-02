from parcial import HistorialDescargas
from reporte import Reporte
from datetime import datetime
import json

class arc:
    def __init__(self,url,tamano,fecha_inicio,estado):
        self.url = url
        self.tamano = tamano
        self.fecha_inicio = fecha_inicio
        self.estado = estado

class principal:
    def __init__(self):
        self.reporte = Reporte()
        self.parcial = HistorialDescargas()
        self.parcial.cargar_descargas_desde_json("descargas.json")
        self.cola_descargas = self.parcial.cola_descargas
        self.historial_completadas = self.parcial.historial_completadas
    
    def cargar_descargas(self, archivo_json):
        self.parcial.cargar_descargas_desde_json(archivo_json)
        self.cola_descargas = self.parcial.cola_descargas
        self.historial_completadas = self.parcial.historial_completadas
    
    def añadir_descarga(self):
        url = input("Ingrese la URL de la descarga: ")
        while(True):
            try:
                tamano = float(input("Ingrese el tamaño de la descarga en MB: "))
                break
            except ValueError:
                print("El tamaño de la descarga debe ser un número.")
        while(True):
            estado = input("Indique el estado que desea visualizar (0 = completado, 1 = pendiente, 2 = en_progreso, 3 = cancelada): ")
            if estado == '0' or estado == '1' or estado == '2' or estado == '3':
                break
            else:
                print("Por favor, introduzca un número válido.")
        match estado:
            case '0':
                estado = "completada"
            case '1':
                estado = "pendiente"
            case '2':
                estado = "en_progreso"
            case '3':
                estado = "cancelada"
        fecha_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nueva_descarga = {"url": url,"tamano": tamano,"fecha_inicio": fecha_inicio,"estado": estado}
        with open("descargas.json", "r") as archivo:
            datos = json.load(archivo)
        datos.append(nueva_descarga)
        with open('descargas.json', 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        self.cargar_descargas("descargas.json")
        print("Datos añadidos exitosamente al archivo JSON.\n")
    
    def run(self):
        seguir = "0"
        while(seguir!="7"):
            print("1. Añadir descarga")
            print("2. Mostrar todas las descargas")
            print("3. Mostrar descargas completadas ordenadas por tamaño")
            print("4. Mostrar descargas sin completar ordenadas por fecha de inicio")
            print("5. Mostrar descargas desde una fecha y url ordenadas por tamaño")
            print("6. Mostrar descargas con un estado ordenadas por la longitud de la URL")
            print("7. Salir")
            seguir = input("Seleccione una opción: ")
            self.cargar_descargas("descargas.json")
            lista = []
            lista.extend(self.cola_descargas)
            lista.extend(self.historial_completadas)
            match seguir:
                case '1':
                    self.añadir_descarga()
                case '2':
                    self.parcial.mostrar_descargas()
                case '3':
                    self.reporte.tamaño_descendente(lista)
                case '4':
                    self.reporte.sinTerminar_ascendente(lista)
                case '5':
                    self.reporte.fecha_heapsort(lista)
                case '6':
                    self.reporte.longitudURL_descendente(lista)
                case '7':
                    print("Saliendo...")
                case _:
                    print("Por favor, introduzca un número válido.")
        print("Fin del programa")

p = principal()
p.run()