# En esta opción disponemos de tres escenarios que no se pueden cambiar
from Escenarios_disponibles import *

class Escenarios():

    def __init__(self,x,y,a,b):
        self.__monedas = x
        self.__miermbros_ekip = y
        self.__movimientos = a
        self.__energia_vital = b

    def get_monedas(self):
        return self.__monedas

    def get_miembros_ekip(self):
        return self.__miermbros_ekip

    def get_movimientos(self):
        return self.__movimientos

    def get_energia_vital(self):
        return self.__energia_vital

    def from_str(x):

        if type(x) != str:
            raise TypeError('El formato de entrada no es correcto')
        nombre_escenario = x.lower()
        escenario_elegido = None

        for tp in TipoEscenario:
            if nombre_escenario == tp.name:
                a = tp.value
                escenario_elegido = Escenarios(a[0], a[1], a[2], a[3])
                break

        if type(escenario_elegido) != Escenarios:
            raise ValueError("No se ha introducido bien el nombre de ningún escenario")

        return escenario_elegido

