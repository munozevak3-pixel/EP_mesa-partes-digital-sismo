"""Módulo de operaciones: registrar, buscar y ordenar expedientes."""

import clasificacion as cla

TIPOS = {"1": "Daño", "2": "Ayuda", "3": "Atención"}


def generar_codigo(codigos, anio):
  """Código correlativo con formato SIS-AAAA-0001."""
  return f"SIS-{anio}-{len(codigos) + 1:04d}"


def registrar(
    datos,
    dni,
    nombre,
    distrito,
    tipo,
    descripcion,
    personas,
    heridos,
    fecha,
    anio,
):
  """Agrega un expediente a los arreglos paralelos y lo clasifica."""
  if tipo not in TIPOS:
    raise ValueError(f"Tipo no válido: {tipo}")

  num_personas = int(personas)
  heridos_upper = heridos.upper()

  codigo = generar_codigo(datos["codigos"], anio)
  puntaje = cla.calcular_puntaje(
      tipo, num_personas, heridos_upper, descripcion
  )
  prioridad = cla.clasificar(puntaje)

  datos["codigos"].append(codigo)
  datos["dnis"].append(dni)
  datos["nombres"].append(nombre.strip().title())
  datos["distritos"].append(distrito.strip().upper())
  datos["tipos"].append(TIPOS[tipo])
  datos["descripciones"].append(descripcion.strip().replace("|", "/"))
  datos["personas"].append(str(num_personas))
  datos["heridos"].append(heridos_upper)
  datos["fechas"].append(fecha)
  datos["prioridades"].append(prioridad)

  return codigo, prioridad


def buscar_por_codigo(codigos, codigo):
  """Búsqueda secuencial. Devuelve la posición o -1."""
  target = codigo.strip().upper()
  for i, c in enumerate(codigos):
    if c == target:
      return i
  return -1


def _burbuja(claves, datos):
  """Ordenamiento burbuja manteniendo sincronizados todos los arreglos."""
  n = len(claves)
  for i in range(n - 1):
    for j in range(n - 1 - i):
      if claves[j] > claves[j + 1]:
        claves[j], claves[j + 1] = claves[j + 1], claves[j]
        for arr in datos.values():
          arr[j], arr[j + 1] = arr[j + 1], arr[j]


def ordenar_por_codigo(datos):
  _burbuja(list(datos["codigos"]), datos)


def ordenar_por_prioridad(datos):
  """Primero por código y luego por prioridad."""
  ordenar_por_codigo(datos)
  claves = [cla.RANGO[p] for p in datos["prioridades"]]
  _burbuja(claves, datos)


def contar_por_prioridad(prioridades):
  """Cuenta cuántos expedientes hay en cada nivel."""
  conteo = {"CRITICO": 0, "ALTO": 0, "MEDIO": 0, "BAJO": 0}
  for p in prioridades:
    if p in conteo:
      conteo[p] += 1
  return conteo