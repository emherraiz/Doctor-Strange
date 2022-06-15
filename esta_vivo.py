class SerVivo():
    # Le pasamos la vida que tiene al constructor
    def __init__(self, vida):
        self._vida = vida

    # Devuelve True si el personaje esta vivo
    def is_vivo(self):
        return self._vida > 0

    # En caso de que este muerto el presonaje se queda con 0 de vida
    def muerto(self):
        self._vida = 0

    # Un get te permite implementar el valor de vida a una variable fuera de la clase
    def get_vida(self):
        return self._vida

    # Con un set podemos ir cambiando el valor que le pasamos inicialmente al constructor
    def set_vida(self, x):
        self._vida = x

    # En caso de que usemos un print nos mostrará la cantidad de vida
    def __str__(self):
        return f'Vida: {self._vida}'
