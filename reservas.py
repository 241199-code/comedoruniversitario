# reservas.py - RF4 y RF5: reservas y control de aforo
from config import AFORO_MAXIMO
reservas = []
def reservar(estudiante, turno):
    if len([r for r in reservas if r[1] == turno]) >= AFORO_MAXIMO:
        return False
    reservas.append((estudiante, turno))
    return True
