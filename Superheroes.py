from Escenarios import *
import random
from enum import Enum
from Vida import Vida
from Tipo_de_superheroe import Tipo_de_superheroe
from Tipo_de_movimiento import *

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

        # Lanzamos excepción en caso de que el formato de entrada no sea correcto
        if type(tipo) != Tipo_de_superheroe or type(escenario) != Escenario:
            raise TypeError('Formato de tipo no válido')

        self.__tipo = tipo

        # Si el tipo es humano(Value = True(1)) tiene unas stats y si no lo es otras
        # Stats: Inteligencia, fuerza, velocidad, resistencia, proyección de energía y habilidades de lucha
        if tipo.value:
            self.__stats = [random.randint(3,8),random.randint(1,7), random.randint(2,6), random.randint(2,6), random.randint(1,7), random.randint(1,8)]
        else:
            self.__stats = [random.randint(4,7),random.randint(1,8), random.randint(1,8), random.randint(3,8), random.randint(1,8), random.randint(3,7)]



        # Monedas que debe invertir cada jugador para incorporar el heroe a su equipo
        # (monedas_iniciales/numero_miebros)*(suma_valores_parrilla/30)
        self.__coste = (escenario.get_monedas() / escenario.get_n_miembros()) * (sum(self.__stats) / 30)

        # Cálculamos la salud con otra formula, de manera similar al coste
        self._salud = (escenario.get_salud() * self.__stats[3])



    def get_identificador(self):
        return self.__identificador

    def get_alias(self):
        return self.__alias

    def get_movimientos(self):
        return self.__movimientos

    def get_tipo(self):
        return self.__tipo

    def get_stats(self):
        return self.__stats

    def get_coste(self):
        return self.__coste

    def set_movimientos(self, lista_movimientos):
        for movimiento in lista_movimientos:
            if movimiento.get_tipo().value:
                movimiento.set_daño((movimiento.get_daño()/10)*(0.8*self.__stats[1] + 0.25*self.__stats[2] + 0.75*self.__stats[5] + self.__stats[4]))
            else:
                movimiento.get_daño((movimiento.get_daño()/10)*(self.__stats[0] + 0.75*self.__stats[2] + 0.25*self.__stats[5] + 0.2*self.__stats[1]))
            self.__movimientos.append(movimiento)

    def defensa(self, daño):
        self._salud = self._salud - daño
        if self._salud <= 0:
            self.muerto()
            self._salud = 0

    def ataque(self, obj, ronda):
        obj.defensa(self.__movimientos[ronda].get_daño())

    def __str__(self):
        return f'{self.get_identificador()}| Alias: {self.get_alias()}| Tipo: {self.get_tipo().name}| Coste: {self.get_coste()}| Vida: {self.get_vida()}\n'








