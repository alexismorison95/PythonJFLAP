import graphviz as gv


def graficarAF(estados, inicio, final, transiciones, alfabeto=None):
    """
    Funcion para graficar un autómata finito.

    Parametros
    ==========

    estados: Es una lista de estados aceptados por el autómata. \n

    inicio: Son los estados de inicio del fsm. \n

    transiciones: Es una tupla de funciones de transición con tres elementos que son: (a,b,c) donde
    (a,b) son los estados de partida y llegada; mientras que c es la letra que acepta. \n
    
    final: Son los estados finales del autómata. \n

    alfabeto: Es el alfabeto aceptado por el autómata.
    """

    # Creo el grafo y le digo que lo guarde en formato .png
    g = gv.Digraph(format='png')

    # Direccion del grafo, de izquierda a derecha
    g.graph_attr['rankdir'] = 'LR'

    # Cargo los nodos
    g.node('ini', shape="point")
    for e in estados:

        if e[0] in final:
            g.node(name=e[0], label=e[1], shape="doublecircle")

        else:
            g.node(name=e[0], label=e[1])

        if e[0] in inicio:
            g.edge('ini', e[0])

    # Cargo las transiciones 
    for t in transiciones:

        if alfabeto:
            if t[2] not in alfabeto:
                return 0

        g.edge(t[0], t[1], label=str(t[2]))
    
    # Renderizo el grafo y lo guardo
    g.render(view=True, directory="res")


# Ejemplo de uso

# if __name__ == '__main__':

#     alf = [0, 1]

#     estados = ["A","B","C","E","F"]

#     inicial = ["A"]

#     terminal = ("C")

#     transiciones = [("A","B", 1), ("A","E",0), ("A","E",1), ("A","A",1), ("A","D",1), ("F","F",1), ("D","C",1),("B","A",0), ("E","C",0), ("F","D",0), ("C","A",0), ("B","B", 1)]

#     graficarAF(alf, estados, inicial, transiciones, terminal)