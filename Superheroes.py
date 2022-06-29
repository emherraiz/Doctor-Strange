from Escenarios import *
import random
from enum import Enum
from Vida import Vida
from Tipo_de_superheroe import Tipo_de_superheroe

class Superheroe(Vida):
    indice = 0

    def __init__(self, alias, identidad_secreta, tipo, escenario):
        # Le damos in identificador a cada superheroe que va a ir aumentando cada vez que cojamos otro superheroe.
        # Esto lo podemos hacer gracias a que la variable no fue definida en ningún metodo si no que es parte de la propia clase
        self.identificador = Superheroe.indice
        Superheroe.indice += 1

        #
        self.__alias = alias
        self.__identidad_secreta = identidad_secreta

        # La lista de movimientos por el momento permanece vacía aunque la vamos a ir rellenando conforme a los movimientos que nos permita el escenarios
        self.__movimientos = []

        #tipos
        if type(tipo) != Tipo_de_superheroe:
            raise TypeError('Formato no válido')
        #
        self.__coste = (escenario.get_monedas() / escenario.get_n_miembros()) * (sum(self.__parrilla_de_poderes) / 30)





