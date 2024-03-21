# Puzle Lineal con búsqueda en profundidad
from arbol import Nodo

def calcular_distancia(num_actual, indice_actual, num_objetivo, indice_objetivo):
    # Calcula la distancia de Manhattan entre dos números en el puzle
    return abs(num_actual - num_objetivo) + abs(indice_actual - indice_objetivo)

def calcular_heuristica(estado_actual, solucion):
    # Calcula la heurística sumando las distancias para cada número en el estado actual
    heuristica = 0
    for num_actual, num_objetivo in zip(estado_actual, solucion):
        if num_actual != num_objetivo:
            indice_actual = estado_actual.index(num_actual)
            indice_objetivo = solucion.index(num_actual)
            heuristica += calcular_distancia(num_actual, indice_actual, num_objetivo, indice_objetivo)
    return heuristica

def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:        
        nodos_frontera.sort(key=lambda x: calcular_heuristica(x.get_datos(), solucion))  # Ordena la frontera por la heurística
        nodo = nodos_frontera.pop(0)  # Selecciona el nodo con menor heurística
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            # solución encontrada
            solucionado = True
            return nodo
        else:
            # expandir nodos hijo
            dato_nodo = nodo.get_datos()            
            # operador izquierdo
            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                    and not hijo_izquierdo.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_izquierdo)
                hijo_izquierdo.set_padre(nodo)
            # operador central
            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados) \
                    and not hijo_central.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_central)
                hijo_central.set_padre(nodo)
            # operador derecho
            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados) \
                    and not hijo_derecho.en_lista(nodos_frontera):                
                nodos_frontera.append(hijo_derecho)
                hijo_derecho.set_padre(nodo)

if __name__ == "__main__":
    estado_inicial = [4, 3, 2, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    # mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    for elemento in resultado:
        print(elemento)
    #print(resultado)
