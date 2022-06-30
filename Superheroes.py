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
        self.__identificador = Superheroe.indice
        Superheroe.indice += 1

        # El alias y la identidad secreta son otras dos propiedades del superheroe
        self.__alias = alias
        self.__identidad_secreta = identidad_secreta

        # La lista de movimientos por el momento permanece vacía aunque la vamos a ir rellenando conforme a los movimientos que nos permita el escenarios
        self.__movimientos = []

        # Observamos que el tu
        if type(tipo) != Tipo_de_superheroe or type(escenario) != Escenario:
            raise TypeError('Formato de tipo no válido')


        # Monedas que debe invertir cada jugador para incorporar el heroe a su equipo
        # (monedas_iniciales/numero_miebros)*(suma_valores_parrilla/30)
        self.__coste = (escenario.get_monedas() / escenario.get_n_miembros()) * (sum(self.__parrilla_de_poderes) / 30)



    def get_identificador(self):
        return self.__identificador

    def get_alias(self):
        return self.__alias

    def get_movimientos(self):
        return self.__movimientos

    def get_tipo(self):
        return self.__tipo







