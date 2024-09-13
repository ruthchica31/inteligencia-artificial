# Función para realizar el ordenamiento por burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    # Recorrer todos los elementos de la lista
    for i in range(n):
        # La última i posiciones ya están ordenadas
        for j in range(0, n - i - 1):
            # Comparar el elemento actual con el siguiente
            if lista[j] > lista[j + 1]:
                # Intercambiar si están en el orden incorrecto
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
mi_lista = [64, 34, 25, 12, 22, 11, 90]
print("Lista antes de ordenar:", mi_lista)

ordenamiento_burbuja(mi_lista)
print("Lista después de ordenar:", mi_lista)
