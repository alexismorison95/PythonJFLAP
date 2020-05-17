# PythonJFLAP

Programa de consola para manejar autómatas finitos. Permite cargar un archivo de JFLAP para generar una imagen mejor del AF o para usarlo para validar cadenas. <br />

Los archivos .jff van en la carpeta jflaps/ <br />

Las imagenes generadas se guardan en la carpeta res/ <br />

## Forma de usar

* Para graficar un autónoma finito:
  ```
  $ python main.py -g (o --graficar) <./ruta/file>.jff
  ```

* Para validar una cadena:
  ```
  $ python main.py -v (o --validar) <./ruta/file>.jff <cadena a validar o nada si cadena vacia>
  ```

## Resultado

![Resultado.png](https://raw.githubusercontent.com/alexismorison95/PythonJFLAP/master/imagenes/finite_state_machine.gv.png) 