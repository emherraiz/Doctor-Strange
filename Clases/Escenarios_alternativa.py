# Es un ejemplo de una manera alternativa de hacerlo
# El diccionario lo podríamos meter en otro fichero
escenarios = {
'sanctum_sanctorum' : [10000, 10, 10, 100],
'stark_tower' : [20000, 20, 25, 200],
'xavier_school' : [80000, 30, 40, 300]
}

# Obtenemos los nombres de los escenarios del diccionario mediante .keys()
nombres_escenarios = list(escenarios.keys())

class Escenario():

    def __init__(self, nombre_escenario, monedas, miembros_equipo, movimientos, energia_vital):
        # Si lo pusieramos de la forma self.__'Atributo' lo podemos hacer privado
        self.nombre_escenario = nombre_escenario
        self.monedas = monedas
        self.miembros_equipo = miembros_equipo
        self.movimientos = movimientos
        self.energia_vital = energia_vital


    # Los gets nos permiten devolver el valor
    def get_monedas(self):
        return self.monedas

    def get_miembros_equipo(self):
        return self.miembros_equipo

    def get_movimientos(self):
        return self.movimientos

    def get_energia_vital(self):
        return self.energia_vital

    # Elegimos el diccionario que queremos
    def eleccion_de_escenarios(i):
        # Error que mostramos en caso de que se escoja un indice que no pertenezca a ningún diccionario
        if i > len(nombres_escenarios) or i <= 0:
            raise TypeError("Ese escenario no existe")

        escenario = escenarios[nombres_escenarios[i - 1]]

        return Escenario(nombres_escenarios[i - 1], escenario[0], escenario[1], escenario[2], escenario[3])

    def __str__(self):
        return f'Nuestro escenario <{self.nombre_escenario}> tiene las siguientes propiedades:\nMonedas: {self.monedas}\nMiembros_equipo: {self.miembros_equipo}\nMovimientos: {self.movimientos}\nEnergia_vital: {self.energia_vital}'


escenario_elegido = Escenario.eleccion_de_escenarios(3)

print(escenario_elegido)
