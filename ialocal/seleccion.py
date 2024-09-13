# Función para realizar el ordenamiento por selección
def ordenamiento_seleccion(lista):
    n = len(lista)
    # Recorre todos los elementos de la lista
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la parte no ordenada de la lista
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        
        # Intercambia el elemento mínimo encontrado con el primer elemento de la parte no ordenada
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista antes de ordenar:", mi_lista)

ordenamiento_seleccion(mi_lista)
print("Lista después de ordenar:", mi_lista)
