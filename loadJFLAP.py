import xml.etree.ElementTree as ET

def loadJFLAP(source, alfIsInt=False):
    """
    Funcion para cargar desde un archivo .jff de JFLAP el grafo graficado. \n

    Parametros:
    ===========

    source: Ruta del archivo (string). \n
    alfIsInt: Booleano que indica si el alfabeto son numeros.

    Devuelve:
    =========

    estados: Lista de estados. Estructura (id, name) \n
    inicial: Lista de estados iniciales. \n
    final: Lista de estados finales. \n
    transiciones: Lista de transiciones. Estructura (from, to, label)
    """

    estados = []
    inicial = []
    final = []
    transiciones = []

    # Cargo el archivo
    doc = ET.parse(source)
    root = doc.getroot()

    # Cargar estados
    for state in root.iter('state'):

        # Cargo el estado
        estados.append((state.attrib['id'], state.attrib['name']))

        for items in state:

            # Si inicial
            if(items.tag == 'initial'):
                inicial.append(state.attrib['id'])

            # Si final
            if(items.tag == 'final'):
                final.append(state.attrib['id'])

    #Cargo las transiciones
    for trans in root.iter('transition'):

        nodoI = trans[0].text
        nodoF = trans[1].text
        label = trans[2].text

        if (alfIsInt):
            transiciones.append((nodoI, nodoF, int(label)))
        else:
            transiciones.append((nodoI, nodoF, label))


    print('Estados', estados)
    print('Iniciales', inicial)
    print('Finales', final)
    print('Transiciones', transiciones)

    return estados, inicial, final, transiciones