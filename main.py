from graficar import graficarAF
from loadJFLAP import loadJFLAP
from validar import generarDiccionario, validarCadena

# Cargo el archivo JFLAP
estados, inicial, final, transiciones = loadJFLAP(source="jflapArchivos/pares.jff", alfIsInt=False)


# Grafico el AF
graficarAF(estados, inicial, final, transiciones)

print()

# Genero el diccionario del AF
dicc = generarDiccionario(transiciones)

# Valido una cadena
cadena = "aaa"

res = validarCadena(cadena, dicc, inicial[0], final)

if res:
    print("La cadena '{}' es valida".format(cadena))
else:
    print("La cadena '{}' es no valida".format(cadena))

