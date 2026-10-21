# PARTE 5 DEL CODIGO

"""Mesa de Partes Digital-Sismo - prototipo inicial (avance EP)."""

from datetime import datetime

import validaciones as val

import expedientes as exp

import archivos as arc





def pedir_dato(mensaje, validador, error):

  """Repite la pregunta hasta que el dato sea válido."""

  while True:

    dato = input(mensaje)

    if validador(dato):

      return dato

    print(" [!] " + error)





def mostrar(d, i):

  print(f" [{d['prioridades'][i]}] {d['codigos'][i]} | {d['nombres'][i]} | "

     f"{d['distritos'][i]} | {d['tipos'][i]} | {d['personas'][i]} pers. | "

     f"{d['descripciones'][i]}")





def menu():

  datos = arc.cargar()

  anio = datetime.now().year

  opcion = ""

  while opcion != "6":

    print("\n=== MESA DE PARTES DIGITAL-SISMO ===")

    print("1. Registrar 2. Buscar por código 3. Ordenar por prioridad")

    print("4. Listar  5. Resumen      6. Salir")

    opcion = input("Opción: ").strip()

    

    if opcion == "1":

      dni = pedir_dato("DNI (8 dígitos): ", val.validar_dni, "DNI inválido.")

      nom = pedir_dato("Nombre completo: ", val.validar_nombre, "Nombre inválido.")

      dis = pedir_dato("Distrito: ", val.validar_distrito, "Distrito no registrado.")

      tip = pedir_dato("Tipo (1 Daño, 2 Ayuda, 3 Atención): ", val.validar_tipo, "Elija 1, 2 o 3.")

      des = pedir_dato("Descripción (10-150 caracteres): ", val.validar_descripcion, "Longitud inválida.")

      per = pedir_dato("Personas afectadas: ", val.validar_personas, "Número de 0 a 500.")

      her = pedir_dato("¿Hay heridos? (S/N): ", val.validar_si_no, "Responda S o N.")

      fec = pedir_dato("Fecha (dd/mm/aaaa): ", val.validar_fecha, "Fecha inválida.")

      

      cod, pri = exp.registrar(datos, dni, nom, dis, tip, des, per, her, fec, anio)

      arc.guardar(datos)

      print(f" Registrado: {cod} - Prioridad: {pri}")

      

    elif opcion == "2":

      pos = exp.buscar_por_codigo(datos["codigos"], input("Código: "))

      if pos == -1:

        print(" Expediente no encontrado.")

      else:

        mostrar(datos, pos)

        

    elif opcion == "3":

      exp.ordenar_por_prioridad(datos)

      arc.guardar(datos)

      print(" Ordenado: críticos primero.")

      

    elif opcion == "4":

      if not datos["codigos"]:

        print(" No hay expedientes.")

      for i in range(len(datos["codigos"])):

        mostrar(datos, i)

        

    elif opcion == "5":

      c = exp.contar_por_prioridad(datos["prioridades"])

      for nivel in c:

        print(f" {nivel}: {c[nivel]}")

        

    elif opcion != "6":

      print(" Opción no válida.")





if __name__ == "__main__":

  menu()