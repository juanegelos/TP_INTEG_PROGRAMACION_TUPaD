import random
import timeit

# --- Funciones de Búsqueda ---

# 1. Búsqueda Lineal Iterativa
def busqueda_lineal(lista, valor_objetivo):
    for i in range(len(lista)):
        if lista[i] == valor_objetivo:
            return i
    return -1

# 2. Búsqueda Binaria Iterativa
def busqueda_binaria_iterativa(lista_ordenada, valor_objetivo):
    bajo = 0
    alto = len(lista_ordenada) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        valor_en_medio = lista_ordenada[medio]
        if valor_en_medio == valor_objetivo:
            return medio
        elif valor_objetivo < valor_en_medio:
            alto = medio - 1
        else:
            bajo = medio + 1
    return -1

# 3. Búsqueda Binaria Recursiva
def busqueda_binaria_recursiva(lista_ordenada, valor_objetivo, bajo, alto):
    if bajo > alto:
        return -1
    medio = (bajo + alto) // 2
    valor_en_medio = lista_ordenada[medio]
    if valor_en_medio == valor_objetivo:
        return medio
    elif valor_objetivo < valor_en_medio:
        return busqueda_binaria_recursiva(lista_ordenada, valor_objetivo, bajo, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista_ordenada, valor_objetivo, medio + 1, alto)

# --- Preparación de los Datos ---

# Generar una lista grande y ordenarla
data_grande = [random.randint(1, 10000000000) for _ in range(100000)]
data_grande.sort() # Necesario para búsqueda binaria

# Lista pequeña predefinida y ordenada
data_pequena = [1, 2, 4, 5, 12, 21, 23, 32, 33, 45, 54, 64, 78, 85, 96, 101, 202, 212]
# Originalmente: [5,4,23,2,1,45,212,32,54,33,85,96,78,64,101,202,12,21]
# Ya está ordenada manualmente aquí para evitar data_pequena.sort() repetido.

# --- Función Auxiliar para Ejecutar y Medir ---
def medir_y_mostrar(nombre_metodo, funcion_busqueda, lista, valor_objetivo, *args):
    """Ejecuta una función de búsqueda y mide su tiempo de ejecución."""
    start_time = timeit.default_timer()
    # Pasa los args adicionales que la función pueda necesitar (ej. bajo, alto para recursivas)
    resultado = funcion_busqueda(lista, valor_objetivo, *args)
    end_time = timeit.default_timer()
    tiempo = end_time - start_time

    estado = "encontrado" if resultado != -1 else "no encontrado"
    print(f"  {nombre_metodo}: {tiempo:.8f} segundos ({estado})")

# --- Ejecución y Comparación ---

print("--- Comparación de Métodos de Búsqueda ---")

# Elementos de prueba (para simular el peor caso, generalmente al final o no existente)
target_existente_grande = data_grande[-1]
target_no_existente_grande = 10000000000 + 1 # Un número fuera del rango

target_existente_pequena = data_pequena[-1]
target_no_existente_pequena = 999

# Búsqueda Lineal
print("\n### Búsqueda Lineal (Iterativa) ###\n")
print("--- Lista Pequeña ---")
medir_y_mostrar("Lineal (existente)", busqueda_lineal, data_pequena, target_existente_pequena)
medir_y_mostrar("Lineal (no existente)", busqueda_lineal, data_pequena, target_no_existente_pequena)
print("\n--- Lista Grande ---")
medir_y_mostrar("Lineal (existente)", busqueda_lineal, data_grande, target_existente_grande)
medir_y_mostrar("Lineal (no existente)", busqueda_lineal, data_grande, target_no_existente_grande)

# Búsqueda Binaria Iterativa
print("\n### Búsqueda Binaria (Iterativa) ###\n")
print("--- Lista Pequeña ---")
medir_y_mostrar("Binaria Iterativa (existente)", busqueda_binaria_iterativa, data_pequena, target_existente_pequena)
medir_y_mostrar("Binaria Iterativa (no existente)", busqueda_binaria_iterativa, data_pequena, target_no_existente_pequena)
print("\n--- Lista Grande ---")
medir_y_mostrar("Binaria Iterativa (existente)", busqueda_binaria_iterativa, data_grande, target_existente_grande)
medir_y_mostrar("Binaria Iterativa (no existente)", busqueda_binaria_iterativa, data_grande, target_no_existente_grande)

# Búsqueda Binaria Recursiva
print("\n### Búsqueda Binaria (Recursiva) ###\n")
print("--- Lista Pequeña ---")
medir_y_mostrar("Binaria Recursiva (existente)", busqueda_binaria_recursiva, data_pequena, target_existente_pequena, 0, len(data_pequena) - 1)
medir_y_mostrar("Binaria Recursiva (no existente)", busqueda_binaria_recursiva, data_pequena, target_no_existente_pequena, 0, len(data_pequena) - 1)
print("\n--- Lista Grande ---")
# Para la búsqueda binaria recursiva en listas grandes, es importante el límite de recursión de Python.
# Si la lista fuera *mucho* más grande, esta versión podría fallar con un RecursionError.
medir_y_mostrar("Binaria Recursiva (existente)", busqueda_binaria_recursiva, data_grande, target_existente_grande, 0, len(data_grande) - 1)
medir_y_mostrar("Binaria Recursiva (no existente)", busqueda_binaria_recursiva, data_grande, target_no_existente_grande, 0, len(data_grande) - 1)