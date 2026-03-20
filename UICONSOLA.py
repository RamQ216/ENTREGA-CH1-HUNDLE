class Matriz:
    def __init__(self):
        # Mantengo tus nombres de variables
        self.fila = int(input("ingrese un numero de filas: "))
        self.columna = int(input("ingrese un numero de columnas: "))
        self.__tablero = [] # Encapsulado con __ para cumplir el requisito

    @property
    def tablero(self):
        return self.__tablero

    def crear(self):
        self.__tablero = [["." for _ in range(self.columna)] for _ in range(self.fila)]
        return self.__tablero
    
    def mostrar(self):
        for i in self.__tablero:
            print(" ".join(i))
