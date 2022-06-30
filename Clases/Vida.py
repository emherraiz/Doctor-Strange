class Vida():
    # Le pasamos la vida que tiene al constructor
    def __init__(self, salud):
        self._salud = salud

    # Devuelve True si el personaje esta vivo
    def is_vivo(self):
        return self._salud > 0

    # Devuelve True si el personaje esta muerto
    def is_muerto(self):
        return self._salud <= 0

    # En caso de que este muerto el presonaje se queda con 0 de vida
    def muerto(self):
        self._salud = 0

    # Un get te permite implementar el valor de vida a una variable fuera de la clase
    def get_vida(self):
        return self.Sal_salud

    # Con un set podemos ir cambiando el valor que le pasamos inicialmente al constructor
    def set_vida(self, x):
        self._salud = x

    # En caso de que usemos un print nos mostrará la cantidad de vida
    def __str__(self):
        return f'Vida: {self._salud}'
