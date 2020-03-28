from graficar import graficarAF
from loadJFLAP import loadJFLAP

# Cargo desde
estados, inicial, final, transiciones = loadJFLAP(source="jflapArchivos/prueba2.jff", alfIsInt=True)

graficarAF(estados, inicial, final, transiciones)