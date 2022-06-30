from enum import Enum
class Tipo_de_superheroe(Enum):
    # Tipos de superheroe
    Humano = 1
    Nohumano = 0

    # Como solo tenemos dos tendremos que pasar un indice 1 o 0
    def from_index(indice):
        if indice == 1 or indice == 0:
            for tipo in Tipo_de_superheroe:
                if tipo.value == indice:
                    tipo_elegido = tipo
                    break

        else:
            raise TypeError('Solo tenemos dos indices, 1 y 0')

        # Nos devuelve el tipo en formato (Clave / valor)
        return tipo_elegido
