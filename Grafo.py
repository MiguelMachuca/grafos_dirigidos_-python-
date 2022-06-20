
"""
Titulo: Estructura de datos de tipo abstracto que consiste en un conjunto de vertices y
un conjunto de aristas que establecen relaciones entre los vertices
Autor: Miguel Angel Machuca Yavita
Fecha: 10/06/2022
Version: 2.0
"""

    
# ¿ implementar los metodos de camino mas corto y costo minimo sobre las estructura de grafos?
import sys
from priodict import priorityDictionary

class Grafo:  # Método crear instancia de la clase Arbol {objeto} establecer valor de tipo objeto
    
    def __init__(self, maximo=50):
        self.maximo = maximo
        self.matriz = [[0] * self.maximo for i in range(self.maximo)]
        self.vector = []
        self.numero = -1
        self.marca = []

    # Métodos de las Clase Grafo
    def crear_vertice(self, nombre):
        if self.numero+1 == self.maximo:
            raise TypeError("Ya llegó al limite de vertices")
        self.numero += 1
        self.vector.append(nombre)

    def cantidad_vertice(self):
        return self.numero + 1

    def es_vertice_valido(self, vertice):
        return vertice >= 0 and vertice <= self.numero

    def insertar_arco(self, u_vertice, v_vertice, peso):
        vertice_u = self.vector.index(u_vertice)
        vertice_v = self.vector.index(v_vertice)
        if not self.es_vertice_valido(vertice_u) or not self.es_vertice_valido(vertice_v):
            print("No es un vertice valido")
            return
        self.matriz[vertice_u][vertice_v] = peso
        self.matriz[vertice_v][vertice_u] = peso

    def eliminar_arco(self, vertice_u, vertice_v):
        if not self.es_vertice_valido(vertice_u) or not self.es_vertice_valido(vertice_v):
            print("No es un vertice valido")
            return
        self.matriz[vertice_u][vertice_v] = 0
        self.matriz[vertice_v][vertice_u] = 0    

    def desmarcar_todos(self,):
        for i in range(self.numero):
            self.marca[i] = False

    def marcar(self, vertice_u):
        if self.es_vertice_valido(vertice_u):
            self.marca[vertice_u] = True

    def desmarcar(self, vertice_u):
        if self.es_vertice_valido(vertice_u):
            self.marca[vertice_u] = False

    def es_marcado(self, vertice_u): # Devuelve true, si el vertice u está marcado
        return self.marca[vertice_u]

    def get_arco(self,  u_vertice, v_vertice):
        vertice_u = self.vector.index(u_vertice)
        vertice_v = self.vector.index(v_vertice)
        return self.matriz[vertice_u][vertice_v]

    def lista_vertice(self):
        return self.vector

    def pSol(self, dist):
        print("Distancia del vertice desde la fuente")
        for vertice in range(self.maximo):
            print(vertice, "t", dist[vertice])

    def minDistance(self, dist, sptSet):

        min = sys.maxsize

        for v in range(self.maximo):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def Dijkstra(self, G,start,end=None):

        D = {}	# dictionary of final distances
        P = {}	# dictionary of predecessors
        Q = priorityDictionary()   # est.dist. of non-final vert.
        Q[start] = 0
        
        for v in Q:
            D[v] = Q[v]
            if v == end: break
            
            for w in G[v]:
                vwLength = D[v] + G[v][w]
                if w in D:
                    if vwLength < D[w]:
                        raise ValueError
                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v
        
        return (D,P)

    def shortestPath(self, G,start,end):

        D,P = self.Dijkstra(G,start,end)
        Path = []
        while 1:
            Path.append(end)
            if end == start: break
            end = P[end]
        Path.reverse()
        return Path


    def mostrar_matriz(self):
        print("La matriz es la siguiente:")
        for i in self.matriz:
            print(i)





