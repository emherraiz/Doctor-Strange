from enum import Enum
# Los escenarios tienen diferentes atributos:
    # Monedas
    # Numero de integrantes de cada equipo
    # Numero de movimientos permitidos
    # Salud
class TipoEscenario(Enum):
    sanctum_sanctorum = [10000, 10, 3, 100]
    stark_tower = [20000, 20, 25, 200]
    xavier_school = [80000, 30, 40, 300]


