# Implementacion que tienen que ser ejecutadas en el main()
from Grafo import *


def main():
    #Ejemplo de arbol, introduciendo valores al arbol
    MyGrafo = Grafo(6)
    MyGrafo.crear_vertice("a")
    MyGrafo.crear_vertice("b")
    MyGrafo.crear_vertice("c")
    MyGrafo.crear_vertice("d")
    MyGrafo.crear_vertice("e")
    MyGrafo.crear_vertice("f")

    MyGrafo.mostrar_matriz()

    MyGrafo.insertar_arco("c", "f", 50)

    MyGrafo.insertar_arco("a", "b", 30)

    MyGrafo.insertar_arco("e", "f", 60)

    print(MyGrafo.cantidad_vertice())

    print(MyGrafo.get_arco("c", "f"))

    print(MyGrafo.lista_vertice())

    MyGrafo.mostrar_matriz()



if __name__ == '__main__':
    main()
