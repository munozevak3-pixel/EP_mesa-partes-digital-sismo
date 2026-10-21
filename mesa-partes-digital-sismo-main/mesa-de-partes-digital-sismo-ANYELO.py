"""Módulo de persistencia: lectura y escritura en archivo de texto."""

import os



RUTA = "reportes_sismo.txt"

CAMPOS = ["codigos", "dnis", "nombres", "distritos", "tipos",

     "descripciones", "personas", "heridos", "fechas", "prioridades"]





def nuevo_almacen():

  """Crea el diccionario de arreglos paralelos vacíos."""

  return {campo: [] for campo in CAMPOS}





def guardar(datos, ruta=RUTA):

  """Escribe un expediente por línea, campos separados por '|'."""

  with open(ruta, "w", encoding="utf-8") as f:

    for i in range(len(datos["codigos"])):

      f.write("|".join(datos[c][i] for c in CAMPOS) + "\n")





def cargar(ruta=RUTA):

  """Lee el archivo y rellena los arreglos paralelos."""

  datos = nuevo_almacen()

  if not os.path.exists(ruta):

    return datos

  with open(ruta, "r", encoding="utf-8") as f:

    for linea in f:

      partes = linea.strip().split("|")

      if len(partes) == len(CAMPOS):

        for k in range(len(CAMPOS)):

          datos[CAMPOS[k]].append(partes[k])

  return datos

