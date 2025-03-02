# algoritmos-de-ordenamiento

Tarea número 3 de algoritmos y estructuras 2. Ejercicio de algoritmos de ordenamiento (quicksort, mergesort, heapsort, shellsort)

Pasos para ejecutar el proyecto:
- clonar el repositorio en el equipo, o copiar los archivos main.py, parcial.py, reporte.py y descargas.json

- Ejecutar main.py

  con ello, abrirá un menu en cmd, donde se podrá interactuar con el programa. El menú posee las siguientes opciones:
  
  1 - Añadir descarga: con esto, se podrá añadir una nueva descarga al archivo descargas.json

  2 - Mostrar todas las descargas: Podrá observar todas las descargas dentro del archivo descargas.json, separadas según sea su estado (completadas o no completadas)

  3 - Mostrar descargas completadas ordenadas por tamaño: Listará las descargas completadas de forma descendente por tamaño utilizando el algoritmo quicksort permitiendo a los usuarios identificar rápidamente los archivos más grandes

  4 - Mostrar descargas sin completar ordenadas por fecha de inicio: Listará las descargas que no han sido completadas de forma ascendente por fecha de inicio (YYYY-MM-DD HH:MM) utilizando el algoritmo mergesort

  5 - Mostrar descargas desde una fecha y url ordenadas por tamaño: Listará las descargas a partir de una fecha (YYYY-MM-DD HH:MM) introducida por el usuario ordenadas de forma ascendente según su tamaño cuya url pertenezca a un dominio especificado por el usuario. Utiliza el algoritmo heapsort

  6 - Mostrar descargas con un estado ordenadas por la longitud de la URL: Listará las descargar de forma descendente según la longitud de su url, además de que debe cumplir un estado indicado por el usuario (0 = completado, 1 = pendiente, 2 = en_progreso, 3 = cancelada) Utiliza el algoritmo shellsort

  7 - Salir: Finaliza el programa
