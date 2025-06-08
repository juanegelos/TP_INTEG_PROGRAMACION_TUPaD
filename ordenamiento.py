import random 
import timeit
from generador_lista import generar_lista_desde_txt

# Generar una lista a partir de un archivo .txt
#archivo="personas1.txt"
#data=generar_lista_desde_txt(archivo)
#random.shuffle(data)
# Generar una lista aleatoria de tamaño 1000
data=[random.randint(1, 10000000000) for _ in range(10000)] 
data_little = [5,4,23,2,1,45,212,32,54,33,85,96,78,64,101,202,12,21]
data1 = data.copy()
data_little1 = data_little.copy()
data2 = data.copy()
data_little2 = data_little.copy()
data3 = data.copy()
data_little3 = data_little.copy()
data4 = data.copy()
data_little4 = data_little.copy()

# Metodo de ordenamiento por Burbuja
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Medir el tiempo de ejecución para pequeños sets de datos
start_time_bubble_l = timeit.default_timer()
bubble_sort(data_little)
end_time_bubble_l = timeit.default_timer()

# Medir el tiempo de ejecución para grandes sets de datos
start_time_bubble = timeit.default_timer()
bubble_sort(data)
end_time_bubble = timeit.default_timer()

# Metodo de ordenamiento por Selección

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i  # Encontrar el índice del elemento mínimo
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Medir tiempo para lista pequeña
start_time_selec_l = timeit.default_timer()
selection_sort(data_little1)
end_time_selec_l = timeit.default_timer()

# Medir tiempo para lista grande
start_time_selec = timeit.default_timer()
selection_sort(data1)
end_time_selec = timeit.default_timer()

# Metodo de ordenamiento por Inserción

def insertion_sort(lista):
  for i in range(1, len(lista)):
    key = lista[i]
    j = i-1
    while j >=0 and key < lista[j] :
        lista[j+1] = lista[j]
        j -= 1
    lista[j+1] = key

# Medir tiempo para la lista pequeña
start_time_ins_l = timeit.default_timer()
insertion_sort(data_little2)
end_time_ins_l = timeit.default_timer()

# Medir tiempo para la lista grandes
start_time_ins = timeit.default_timer()
insertion_sort(data2)
end_time_ins = timeit.default_timer()

# Metodo de ordenamiento Quicksort Recursivo

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Medir tiempo para lista pequeña
start_time_q_l = timeit.default_timer()
r_data_little3=quicksort(data_little3)
end_time_q_l = timeit.default_timer()

# Medir tiempo para lista grande
start_time_q = timeit.default_timer()
r_data3=quicksort(data3)
end_time_q = timeit.default_timer()

# Metodo de ordenamiento Quicksort Iterativo

def quick_sort_iterativo(lista):
    if len(lista) <= 1:
        return lista
    pila = [(0, len(lista)-1)]
    while pila:
        inicio, fin = pila.pop()
        if inicio >= fin:
            continue
        pivot = lista[fin]
        i = inicio
        for j in range(inicio, fin):
            if lista[j] < pivot:
                lista[i], lista [j] = lista[j], lista [i]
                i += 1
        lista[i], lista[fin] = lista[fin], lista[i]
        pila.append((inicio, i-1))
        pila.append((i+1, fin))
    return lista

# Medir tiempo para lista pequeña
start_time_qi_l = timeit.default_timer()
quick_sort_iterativo(data_little4)
end_time_qi_l = timeit.default_timer()

# Medir tiempo para lista grande
start_time_qi = timeit.default_timer()
quick_sort_iterativo(data4)
end_time_qi = timeit.default_timer()


print("Impresion tiempos de respuesta de todos los métodos implementados\n")
print("\n[BURBUJA] Tiempo de ejecución para la lista pequeña fue de:", end_time_bubble_l - start_time_bubble_l, "segundos")
print("[BURBUJA] Tiempo de ejecución para lista grande:", end_time_bubble - start_time_bubble, "segundos\n")
print("[SELECCION] Tiempo para una lista pequeña:", end_time_selec_l - start_time_selec_l, "segundos")
print("[SELECCION] Tiempo para una lista grande:", end_time_selec - start_time_selec, "segundos\n")
print("[INSERCION] Tiempo para lista pequeña:", end_time_ins_l - start_time_ins_l, "segundos")
print("[INSERCION] Tiempo para lista grande:", end_time_ins - start_time_ins, "segundos\n")
print("[QUICKSORT] Tiempo para una lista pequeña:", end_time_q_l - start_time_q_l, "segundos")
print("[QUICKSORT] Tiempo para una lista grande:", end_time_q - start_time_q, "segundos\n")
print("[QUICKSORT ITER] Tiempo para una lista pequeña:", end_time_qi_l - start_time_qi_l, "segundos")
print("[QUICKSORT ITER] Tiempo para una lista grande:", end_time_qi - start_time_qi, "segundos\n")

print("Impresion de las listas ordenadas - LISTAS PEQUEÑAS\n")
print("Lista pequeña ordenada por método BURBUJA")
print(data_little,"\n")
print("Lista pequeña ordenada por método SELECCION")
print(data_little1,"\n")
print("Lista pequeña ordenada por método INSERCION")
print(data_little2,"\n")
print("Lista pequeña ordenada por método QUICKSORT Recursivo")
print(r_data_little3,"\n")
print("Lista pequeña ordenada por método QUICKSORT Iterativo")
print(data_little4,"\n")

"""
print("Impresion de las listas ordenadas - LISTAS GRANDES\n")
print("Lista grande ordenada por método BURBUJA")
print(data,"\n")
print("Lista grande ordenada por método SELECCION")
print(data1,"\n")
print("Lista grande ordenada por método INSERCION")
print(data2,"\n")
print("Lista grande ordenada por método QUICKSORT Recursivo")
print(r_data3,"\n")
print("Lista grande ordenada por método QUICKSORT Iterativo")
print(data4,"\n")
"""