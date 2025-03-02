from datetime import datetime

class Reporte:
    def __init__(self):
        pass
    
    def tamaño_descendente(self, descargas:list):
        quick_sort(descargas,0,len(descargas)-1)
        print("\nURL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in descargas:
            if descarga.estado == 'completada':
                print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        print("")
    
    def sinTerminar_ascendente(self, descargas:list):
        for elemento in descargas:
            print(elemento.url)
        print("----------------------------------------------------------------------------------")
        ordenado = merge_sort(descargas)
        for elemento in ordenado:
            print(elemento.url)
        print("\nURL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in ordenado:
            if descarga.estado != 'completada':
                print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        print("")
    
    def fecha_heapsort(self, lista:list):
        while(True):
            try:
                fecha_hora_usuario = input("Introduce una fecha y hora (YYYY-MM-DD HH:MM): ")
                fecha_usuario = datetime.strptime(fecha_hora_usuario, "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("El formato de la fecha y hora es incorrecto. Por favor, utiliza el formato: YYYY-MM-DD HH:MM")
        dominio = input("Escriba el domínio a buscar: ")
        heapSort(lista)
        print("\nURL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in lista:
            fecha_descarga = datetime.strptime(descarga.fecha_inicio, "%Y-%m-%d %H:%M:%S")
            if (fecha_descarga >= fecha_usuario) and (dominio in descarga.url):
                print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        print("")
    
    def longitudURL_descendente(self, lista:list):
        estado=""
        while(True):
            estado = input("Indique el estado que desea visualizar (0 = completado, 1 = pendiente, 2 = en_progreso, 3 = cancelada): ")
            if estado == '0' or estado == '1' or estado == '2' or estado == '3':
                break
            else:
                print("Por favor, introduzca un número válido.")
        shellSort(lista, len(lista))
        match estado:
            case '0':
                estado = "completada"
            case '1':
                estado = "pendiente"
            case '2':
                estado = "en_progreso"
            case '3':
                estado = "cancelada"
        print("\nURL                                          Tamaño MB     Fecha de Inicio    Estado")
        for descarga in lista:
            if descarga.estado == estado:
                print("{0:40s} {1:10.2f} MB {2:19s} {3}".format(descarga.url,descarga.tamano,descarga.fecha_inicio,descarga.estado))
        print("")


# pregunta 1, orden por quicksort
def quick_sort(lista,izq,der):
    if izq < der:
        piv = particion(lista,izq,der)
        quick_sort(lista,izq,piv-1)
        quick_sort(lista,piv+1,der)

def particion(lista,izq,der):
    piv = lista[der].tamano
    menor = izq - 1
    for k in range(izq,der):
        if lista[k].tamano >= piv:
            menor += 1
            lista[menor], lista[k] = lista[k], lista[menor]
    menor += 1
    lista[menor], lista[der] = lista[der], lista[menor]
    return menor

#pregunta 2, orden por mergesort
def merge_sort(lista):
    if len(lista) == 1:
        return lista
    medio = len(lista)//2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    izquierdaOrd = merge_sort(izquierda)
    derechaOrd = merge_sort(derecha)
    return merge(izquierdaOrd,derechaOrd)

def merge(izquierda,derecha):
    resultado = []
    while(len(izquierda) > 0 and len(derecha) > 0):
        tIzq = izquierda[0].fecha_inicio
        tDer = derecha[0].fecha_inicio
        tiempoIzq = datetime.strptime(tIzq, "%Y-%m-%d %H:%M:%S")
        tiempoDer = datetime.strptime(tDer, "%Y-%m-%d %H:%M:%S")
        if tiempoIzq <= tiempoDer:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    
    if len(izquierda) > 0:
        resultado.append(izquierda.pop(0))
    if len(derecha) > 0:
        resultado.extend(derecha)
    return resultado

#pregunta 3, orden por heapsort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and arr[i].fecha_inicio < arr[l].fecha_inicio:
        largest = l
    if r < n and arr[largest].fecha_inicio < arr[r].fecha_inicio:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#pregunta 4, orden por shellsort
def shellSort(lista, pos):
    interval = pos // 2
    while interval > 0:
        for i in range(interval, pos):
            temp = lista[i]
            j = i
            while j >= interval and len(lista[j - interval].url) < len(temp.url):
                lista[j] = lista[j - interval]
                j -= interval
            lista[j] = temp
        interval //= 2