# Crear un grafo vacío usando un diccionario
grafo = {}

# Función para agregar un vértice al grafo
def agregar_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []

# Función para agregar una arista al grafo (enlace entre dos vértices)
def agregar_arista(grafo, vertice1, vertice2):
    if vertice1 in grafo and vertice2 in grafo:
        grafo[vertice1].append(vertice2)
        grafo[vertice2].append(vertice1)  # Eliminar esta línea para un grafo dirigido

# Función para imprimir el grafo
def imprimir_grafo(grafo):
    for vertice, adyacentes in grafo.items():
        print(f"{vertice}: {adyacentes}")

# Ejemplo de uso
# Agregar vértices al grafo
agregar_vertice(grafo, 'A')
agregar_vertice(grafo, 'B')
agregar_vertice(grafo, 'C')
agregar_vertice(grafo, 'D')

# Agregar aristas entre los vértices
agregar_arista(grafo, 'A', 'B')
agregar_arista(grafo, 'A', 'C')
agregar_arista(grafo, 'B', 'D')
agregar_arista(grafo, 'C', 'D')

# Imprimir el grafo
print("Grafo:")
imprimir_grafo(grafo)
