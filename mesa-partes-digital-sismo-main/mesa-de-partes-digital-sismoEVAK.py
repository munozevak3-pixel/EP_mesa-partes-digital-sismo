from datetime import datetime
import os

DISTRITOS = ["ANCON", "ATE", "BARRANCO", "BREÑA", "CALLAO", "CARABAYLLO", "COMAS",
             "INDEPENDENCIA", "LOS OLIVOS", "LURIN", "MIRAFLORES", "PUENTE PIEDRA",
             "RIMAC", "SAN JUAN DE LURIGANCHO", "SAN MARTIN DE PORRES",
             "SANTA ROSA", "SURCO", "VILLA EL SALVADOR", "VILLA MARIA DEL TRIUNFO", "EL AGUSTINO"]


def validar_dni(dni):
    """El DNI debe tener exactamente 8 dígitos numéricos."""
    return len(dni) == 8 and dni.isdigit()


def validar_nombre(nombre):
    """Solo letras y espacios, mínimo 3 caracteres."""
    limpio = nombre.strip()
    return len(limpio) >= 3 and all(c.isalpha() or c == " " for c in limpio)


def validar_distrito(distrito):
    """El distrito debe estar en la lista de distritos registrados."""
    return distrito.strip().upper() in DISTRITOS


def validar_tipo(tipo):
    """Tipo de reporte: 1 daño, 2 ayuda, 3 atención."""
    return tipo in ("1", "2", "3")


def validar_descripcion(texto):
    """La descripción debe tener entre 10 y 150 caracteres."""
    return 10 <= len(texto.strip()) <= 150


def validar_personas(texto):
    """Número entero entre 0 y 500."""
    return texto.isdigit() and 0 <= int(texto) <= 500


def validar_si_no(texto):
    return texto.strip().upper() in ("S", "N")


def validar_fecha(fecha):
    """Formato dd/mm/aaaa y fecha real."""
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False


