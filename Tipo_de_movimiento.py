from enum import Enum
# Nuevamente utilizamos Enum para ver seleccionar el tipo de movimiento que utilizaremos
class Movimiento_Type(Enum):
    ATAQUE = 1
    DEFENSA = 0


class Movimientos_General():
    def __init__(self, nombre, tipo, daño):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__daño = daño

    def get_nombre(self):
        return self.__nombre

    def get_tipo(self):
        return self.__tipo

    def get_daño(self):
        return self.__daño

    def set_daño(self, daño):
        self.__daño = daño


# Heredamos de movimientos el constructor, ya que el movimiento específico también tiene estos atributos
class Movimientos_Especifico(Movimientos_General):
    def __init__(self, nombre, tipo, daño, superheroe):
        super().__init__(nombre, tipo, daño)
        self.__superheroe = superheroe

    def get_superheroe(self):
        return self.__superheroe
