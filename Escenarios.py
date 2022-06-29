# En esta opción disponemos de tres escenarios que no se pueden cambiar
from Escenarios_disponibles import *

class Escenarios():

    # En un momento inicial el constructor estará vacío pero más adelante mediante el método from_str(),
    # generamos una nueva instancia en la que le daremos valores a todas variables del constructor con las propiedades del escenario elegido
    def __init__(self, monedas, n_miembros, n_movimientos, salud):
        self.__monedas = monedas
        self.__n_miembros = n_miembros
        self.__n_movimientos = n_movimientos
        self.__salud = salud

    def get_monedas(self):
        return self.__monedas

    def get_n_miembros(self):
        return self.__n_miembros

    def get_n_movimientos(self):
        return self.__n_movimientos

    def get_salud(self):
        return self.__salud

    # Rell
    def from_str(escenario_deseado):

        # El escenario se tiene que elegir introduciendo el nombre por lo que si el formato de entrada no es una cadena se genera una excepción
        if type(escenario_deseado) != str:
            raise TypeError('El formato de entrada no es correcto')

        # Lower para introduzca mayúsculas o minúsculas se corresponda con algún escenario
        nombre_escenario = escenario_deseado.lower()
        escenario_elegido = None
        # Iteramos por los escenarios disponibles gracias a Enum (Clave / Valor)
        for escenario in TipoEscenario:
            if nombre_escenario == escenario.name:
                # a es la lista con las propiedades que tiene cada escenario
                a = escenario.value

                # Por medio de la recursibidad una vez seleccionamos correctamente el escenario,
                # tomaremos una instancia de esta clase la cual devolvemos al final de la función
                escenario_elegido = Escenarios(a[0], a[1], a[2], a[3])
                break

        # En caso de que no se haya introducido un formato correcto se generará una excepción
        if type(escenario_elegido) != Escenarios:
            raise ValueError("No se ha introducido bien el nombre de ningún escenario")

        return escenario_elegido

