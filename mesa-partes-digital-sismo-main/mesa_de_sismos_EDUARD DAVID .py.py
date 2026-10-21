# PARTE 2 DEL CODIGO

"""Módulo innovador: clasificación automática de expedientes por prioridad."""



PALABRAS_GRAVES = ["atrapado", "atrapada", "derrumbe", "colapso", "incendio",

          "fuga de gas", "herido", "sin respirar", "desaparecido"]

RANGO = {"CRITICO": 1, "ALTO": 2, "MEDIO": 3, "BAJO": 4}





def contiene_palabra_grave(descripcion):

  """Recorre la lista de palabras clave dentro de la cadena de texto."""

  texto = descripcion.lower()

  for palabra in PALABRAS_GRAVES:

    if palabra in texto:

      return True

  return False





def calcular_puntaje(tipo, personas, heridos, descripcion):

  """Suma puntos según tipo de reporte, personas, heridos y palabras clave."""

  puntaje = 0

  if tipo == "2":

    puntaje += 3

  elif tipo == "1":

    puntaje += 2

  else:

    puntaje += 1

    

  if personas >= 10:

    puntaje += 3

  elif personas >= 4:

    puntaje += 2

  elif personas >= 1:

    puntaje += 1

    

  if heridos == "S":

    puntaje += 3

    

  if contiene_palabra_grave(descripcion):

    puntaje += 3

    

  return puntaje





def clasificar(puntaje):

  """Convierte el puntaje en CRITICO, ALTO, MEDIO o BAJO."""

  if puntaje >= 8:

    return "CRITICO"

  elif puntaje >= 5:

    return "ALTO"

  elif puntaje >= 3:

    return "MEDIO"

  return "BAJO"