class Organizacion():
    '''Agrupacion de superheroes, aquí tendremos a todos los superheroes que forman el equipo'''
    def __init__(self, nombre, superheroes):
        # Generamos excepciones en caso de que no se introduzcan los datos correctamente
        if type(nombre) != str:
            raise TypeError('Introduce un nombre correcto')
        if type(superheroes) != list:
            raise TypeError('Los superheroes se pasan en forma de lista')
        if len(superheroes) == 0:
            raise ValueError('No se ha introducido ningún superheroe en la organización')

        self.__nombre = nombre
        self.__superheroes = superheroes


    # En las clases tenemos metodos gets y sets para cambiar o devolver los datos del constructor
    def get_nombre(self):
        return self.__nombre

    def get_superheroes(self):
        return self.__superheroes

    def set_superheroes(self, superheroes):
        if type(superheroes) != list or len(superheroes) == 0:
            raise TypeError('Se tiene que introducir una lista no vacía')

        self.__superheroes = superheroes

    # Podemos añadir los superheroes que queramos simplemente con un .append()
    def añadir_superheroes(self, superheroes):
        if type(superheroes) != list or len(superheroes) == 0:
            raise TypeError('Se tiene que introducir una lista no vacía')
        self.__superheroes.append(superheroes)

    # Para cambiar un superheroe simplemente le tenemos que pasar el superheroe que queremos por el indice en la lista del superheroe que queremos reemplazar
    def cambiar_un_superheroes(self, superheroe, posicion):
        if type(superheroe) != str:
            raise TypeError('El superheroe debe ser introducido como una cadena')
        try:
            posicion = int(posicion) - 1
        except:
            print('La posición en la lista del superheroe tiene que ser un número entero')

        if posicion < 0 or posicion > (len(self.__superheroes) - 1):
            raise ValueError('La posición no corresponde con los elementos de la lista')

        self.__superheroes[posicion] = superheroe

    # Eliminamos el superheroe de la posición que le indiquemos
    def eliminar_superheroe(self, posicion):
        try:
            posicion = int(posicion) - 1
        except:
            print('La posición en la lista del superheroe tiene que ser un número entero')

        if posicion < 0 or posicion > (len(self.__superheroes) - 1):
            raise ValueError('La posición no corresponde con los elementos de la lista')

        print(f'El superheroe {self.__superheroes[posicion].get_alias()} ya no forma parte de tú equipo :(')
        self.__superheroes.remove(self.__superheroes[posicion])

    # Esta lista te devuelve True si quedan superheroes vivos
    def is_undefeated(self):
        # Suponemos que estan todos muertos e iteraremos la lista de superheroes comprobandolo, en caso de que haya alguno vivo, esta variable cambia su valor
        todos_muertos = True
        for superheroe in self.__superheroes:
            # Booleano que nos devuelve si la vida del personaje es mayor que 0
            if superheroe.isvivo() and todos_muertos:
                todos_muertos = False

        # Si no estan todos muertos devolvemos un True y el juego continua
        return not todos_muertos

    # Devuelve una lista de todos los superheroes vivos (por defecto) o todos los muertos, según elijas
    def get_superheroes_undefeated(self, devolver_vivos = True):
        lst_superheroes = []
        if devolver_vivos:
            for superheroe in self.__superheroes:
                if superheroe.is_vivo():
                    lst_superheroes.append(superheroe)

        else:
            for superheroe in self.__superheroes:
                if superheroe.is_muerto():
                    lst_superheroes.append(superheroe)

        return lst_superheroes

    # Si la organización se rinde todos los superheroes del equipo mueren
    def surrender(self):
        for superheroe in self.__superheroes:
            superheroe.muerto()

    # Los siguientes dos métodos se inician cuando utilizamos print y nos sirve para mostrar los datos de los superheroes
    # Str devuelve una versión fácil de usar el objeto
    def __str__(self):
        texto_salida = ''
        for superheroe in self.__superheroes:
            texto_salida += f'\t{superheroe.get_identificador()} - {superheroe.get_alias().upper()}\n\t\tTipo: {superheroe.get_tipo().name}\n\t\tCoste: {superheroe.get_coste()}\n\t\tVida: {superheroe.get_vida()}\n\n'


        return texto_salida

    # Repr devuelve la representación de cadena del objeto, enfocada a desarrolladores
    def __repr__(self):
        texto_salida = ''
        for superheroe in self.__superheroes:
            texto_salida += superheroe.get_identificador() + '\n\t' + superheroe.get_alias() + '\n\t'

