# Función para realizar el ordenamiento por inserción
def ordenamiento_insercion(lista):
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]  # Elemento actual a insertar en la parte ordenada
        j = i - 1
        # Mueve los elementos de la parte ordenada que son mayores que la clave
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta la clave en la posición correcta
        lista[j + 1] = clave

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista antes de ordenar:", mi_lista)

ordenamiento_insercion(mi_lista)
print("Lista después de ordenar:", mi_lista)
