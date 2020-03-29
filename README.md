# PythonJFLAP

Programa de consola para manejar autónomas finitos. Permite cargar un archivo de JFLAP para generar una imagen mejor del AF o para usarlo para validar cadenas. <br />

Los archivos .jff van en la carpeta jflaps/ <br />

Las imagenes generadas se guardan en la carpeta res/ <br />

#### Forma de usar:

* Para graficar un autónoma finito:
  ```
  $ python main.py -g (o --graficar) <file>.jff
  ```

* Para validar una cadena:
  ```
  $ python main.py -v (o --validar) <file>.jff <cadena a validar o nada si cadena vacia>
  ```