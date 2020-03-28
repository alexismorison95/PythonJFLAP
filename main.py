from graficar import graficarAF
from loadJFLAP import loadJFLAP
from validar import generarDiccionario, validarCadena

# Cargo el archivo JFLAP
estados, inicial, final, transiciones = loadJFLAP(source="jflapArchivos/pares.jff", alfIsInt=False)

# Grafico el AF
graficarAF(estados, inicial, final, transiciones)


# Genero el diccionario del AF
print()
dicc = generarDiccionario(transiciones)

# Valido una cadena
cadena = "aaaa"
res = validarCadena(cadena, dicc, inicial[0], final)

if res:
    print("La cadena '{}' es valida".format(cadena))
else:
    print("La cadena '{}' no valida".format(cadena))

