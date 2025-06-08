# TP_INTEG_PROGRAMACION_TUPaD
Este repositorio contiene todos los archivos presentados en el Trabajo Practico Integrador de la materia Programación I, correspondiente al primer cuatrimestre de la carrera Tecnicatura Universitaria en Programación a Distancia, dictada por la Universidad Tecnológica Nacional.

Profesor: Ariel Enferrel
Tutor: Ramiro Hualpa
Fecha de Entrega: 9 de junio de 2025.-

Presentado por:
                Israel Garcia Moscoso
                Juan Esteban Gelos

Tema tratado: Algoritmos de Busqueda y ordenamiento


Contenido:
        Programacion TP Integrador.pdf
        Anexo 1.pdf
        Anexo 2.pdf
        busqueda.py
        generador_listas.py
        ordenamiento.py
        personas1.txt

        Video explicativo:  

Repositorio: https://github.com/juanegelos/TP_INTEG_PROGRAMACION_TUPaD.git

Forma de uso archivo ordenamiento.py
Este archivo mide los tiempos de ejecución de 5 algoritmos de ordenamiento (burbuja, inserción, selección, quicksort recursivo y quicksort iterativo). El archivo genera listas numéricas random, a la cual se le puede ir reemplazando la cantidad de elementos que queremos tenga la lista (modificar range en linea 10). Asimismo generamos una lista manual de 18 elementos que también será ordenada (linea 11).
A partir de alli genererá copias exactas de esa lista para que todos los médotos utilicen las mismas listas. Al final muestra por consola los tiempos de respuesta de cada método, tanto para listas pequeñas como para listas grandes y muestra como quedan las listas ordenadas por cada método. 
Para ver el ordenamiento de las listas grandes, tiene que descomentar las lineas 160 a 170.
Otra opción es trabajar con listas de strings. Para ello hay que comentar la linea 10 y descomentar las lineas 6 a 8. Ahora los algoritmos trabajarán con una lista de string y por consola se mostrará los tiempos de respuesta de cada método. Para ver las listas como quedaron ordenadas, descomentar las lineas 160 a 170

Forma de uso archivo busqueda.py
Este archivo mide los tiempos de ejecucón de 3 algoritmos de búsqueda (lineal, binaria iterativa y binaria recursiva). El archivo genera listas numéricas random, a la cual se le puede ir reemplazando la cantidad de elementos que queremos tenga la lista (modificar range en linea 44). Tanto para las listas pequeñas como para las grandes, se le pide que encuentre el último elemento de la lista y que busque un elemento que no está en la lista. Finalmente muestra por consola los tiempos de ejecucón de cada uno de los algoritmos para cada una de las hipótesis planteadas.