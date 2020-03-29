from func.graficar import graficarAF
from func.loadJFLAP import loadJFLAP
from func.validar import generarDiccionario, validarCadena

import sys
import getopt


def comoUsar():
    """
    Funcion que muestra el tutorial de como usar el programa.
    """
    print()
    print("Tutorial")
    print("Graficar AF: python main.py [--graficar, -g] <file>.jff")
    print("Validar una cadena: python main.py [--validar, -v] <file>.jff <cadena a validar o nada si cadena vacia>")


def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hg:v:", ["help", "graficar=", "validar="])
    except getopt.GetoptError as err:
        print()
        print(err)
        comoUsar()
        sys.exit(2)

    for opt, arg in opts:

        # AYUDA
        if opt in ("-h", "--help"):
            comoUsar()
            sys.exit(2)
        
        # GRAFICAR
        elif opt in ("-g", "--graficar"):

            try:
                open(arg, 'r')
            except (OSError, IOError) as e:
                print()
                print(e)
                comoUsar()
                sys.exit(2)
            
            # Cargo el archivo JFLAP
            estados, inicial, final, transiciones = loadJFLAP(source=arg, alfIsInt=False)

            # Grafico el AF y lo guardo en la carpeta res/
            graficarAF(estados, inicial, final, transiciones)

        # VALIDAR CADENA
        elif opt in ("-v", "--validar"):

            try:
                open(arg, 'r')
            except (OSError, IOError) as e:
                print()
                print(e)
                comoUsar()
                sys.exit(2)

            # Cargo el archivo JFLAP
            estados, inicial, final, transiciones = loadJFLAP(source=arg, alfIsInt=False)

            # Genero el diccionario
            dicc = generarDiccionario(transiciones)

            # Valido la cadena
            cad = ""
            if(args):
                cad = args[0]

            res = validarCadena(cad, dicc, inicial[0], final)

            # Muestro el resultado
            if res:
                print("La cadena '{}' es valida".format(cad))
            else:
                print("La cadena '{}' es no valida".format(cad))


if __name__ == '__main__':
    main()