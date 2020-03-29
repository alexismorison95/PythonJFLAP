def generarDiccionario(tran):
    """
    Funcion para generar un diccionario.

    Parametros:
    ==========
    tran: Lista que contiene todas las tranciciones con el formato (from, to, label).

    Retorna:
    =======
    diccionario: Diccionario necesario para evaluar el AF.
    """

    diccionario = {}

    for t in tran:
        diccionario[(t[0], t[2])] = t[1]
    
    return diccionario


def validarCadena(palabra, dicc, inicial, final):
    """
    Funcion para validar una cadena.

    Parametros:
    ==========
    palabra: String de la cadena a validar. \n
    dicc: Diccionario del AF. \n
    inicial: Estado inicial. \n
    final: Lista de estados finales. \n

    Retorna:
    =======
    isValida?: Booleano que indica si la cadena es valida o no.
    """

    if (palabra == ""):

        if (inicial in final):
            return True
        else:
            return False
        
    return validarCadena(palabra[1:], dicc, dicc[inicial, palabra[0]], final)