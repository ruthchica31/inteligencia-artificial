# Función para realizar la búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for indice, valor in enumerate(lista):
        if valor == objetivo:
            return indice  # Devuelve el índice donde se encontró el objetivo
    return -1  # Devuelve -1 si el objetivo no se encuentra en la lista

# Ejemplo de uso
mi_lista = [4, 2, 7, 1, 9, 3]
objetivo = 7

resultado = busqueda_lineal(mi_lista, objetivo)

if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
