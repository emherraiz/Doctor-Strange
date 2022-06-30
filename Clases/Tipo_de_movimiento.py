from Clases.movimientos_base import Movimiento_Type
from Movimientos_general import Movimientos_General

# Heredamos de movimientos el constructor, ya que el movimiento específico también tiene estos atributos
class Movimientos_Especifico(Movimientos_General):
    def __init__(self, nombre, tipo, daño, superheroe):
        super().__init__(nombre, tipo, daño)
        self.__superheroe = superheroe

    def get_superheroe(self):
        return self.__superheroe
