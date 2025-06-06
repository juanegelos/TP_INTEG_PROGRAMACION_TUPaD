import os

def generar_lista_desde_txt(archivo):
    """
    Lee un archivo de texto y devuelve una lista donde cada elemento
    es una línea del archivo, eliminando los saltos de línea.

    Args:
        archivo (str): La ruta completa o el nombre del archivo TXT.

    Returns:
        list: Una lista con el contenido del archivo.
              Devuelve una lista vacía si el archivo no se encuentra.
    """
    lista_generada = []
    try:
        # Abre el archivo en modo lectura ('r')
        with open(archivo, 'r', encoding='utf-8') as archivo:
            # Itera sobre cada línea del archivo
            for linea in archivo:
                # Elimina espacios en blanco y el salto de línea al final de cada línea
                lista_generada.append(linea.strip())
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
    return lista_generada

if __name__ == "__main__":
    archivo="personas.txt"
    print(generar_lista_desde_txt(archivo))
