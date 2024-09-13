# Función para realizar la búsqueda binaria
def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2
        valor_medio = lista[medio]
        
        if valor_medio == objetivo:
            return medio  # Devuelve el índice donde se encontró el objetivo
        elif valor_medio < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    
    return -1  # Devuelve -1 si el objetivo no se encuentra en la lista

# Ejemplo de uso
mi_lista_ordenada = [1, 2, 3, 4, 7, 9]  # La lista debe estar ordenada para la búsqueda binaria
objetivo = 7

resultado = busqueda_binaria(mi_lista_ordenada, objetivo)

if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista.")
