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
