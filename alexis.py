from graficar import graficarAF
from loadJFLAP import loadJFLAP

estados, inicial, final, transiciones = loadJFLAP("prueba2.jff", True)

graficarAF(estados, inicial, final, transiciones)