import random
from abc import ABC, abstractmethod

# 1. ZONA DE DOMINIO (Se agrega la abstracción sin cambiar tu lógica)

class EntidadBase(ABC):
    @abstractmethod
    def colocar(self, matriz_objeto):
        pass


class piso(EntidadBase): # Ahora hereda de la clase abstracta
    def interaccion(self, tablero, x, y):
        if random.random() < 0.2:
            print("\n¡EL SUELO SE ROMPIÓ!")
            tablero[x][y] = "  "
            return False 
        return True

    def colocar(self, matriz_objeto):
        tablero = matriz_objeto.tablero
        max_f = matriz_objeto.fila
        max_c = matriz_objeto.columna
        trampas_puestas = 0
        while trampas_puestas < 6:
            f = random.randint(0, max_f - 1)
            c = random.randint(0, max_c - 1)
            if tablero[f][c] == ".":
                tablero[f][c] = "_"
                trampas_puestas += 1

class piso_lava(piso):
    def interaccion(self, tablero, x, y):
        if random.random() < 0.5:
            print("\n¡LA LAVA TE QUEMÓ!")
            tablero[x][y] = "  "
            return False 
        return True

    def colocar(self, matriz_objeto):
        tablero = matriz_objeto.tablero
        max_f = matriz_objeto.fila
        max_c = matriz_objeto.columna
        trampas_puestas = 0
        while trampas_puestas < 4:
            f = random.randint(0, max_f - 1)
            c = random.randint(0, max_c - 1)
            if tablero[f][c] == ".":
                tablero[f][c] = "__"
                trampas_puestas += 1

class personaje:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.__vidas = 3 # Atributo protegido/privado

    @property
    def vidas(self):
        return self.__vidas
    
    def restar_vida(self):
        self.__vidas -= 1

    def colocar(self, matriz_objeto):
        matriz_objeto.tablero[self.x][self.y] = "H"

    def mover(self, obj_matriz, p_normal, p_lava):
        entrada = input("W:arriba, S:abajo, A:izq, D:derecha, Q=salir: ").upper()
        if entrada == "Q": return "Q"

        nueva_x, nueva_y = self.x, self.y
        if entrada == "W": nueva_x -= 1
        elif entrada == "S": nueva_x += 1
        elif entrada == "A": nueva_y -= 1
        elif entrada == "D": nueva_y += 1

        if 0 <= nueva_x < obj_matriz.fila and 0 <= nueva_y < obj_matriz.columna:
            simbolo_destino = obj_matriz.tablero[nueva_x][nueva_y]
            sobrevive = True

            if simbolo_destino == "_":
                sobrevive = p_normal.interaccion(obj_matriz.tablero, nueva_x, nueva_y)
            elif simbolo_destino == "__":
                sobrevive = p_lava.interaccion(obj_matriz.tablero, nueva_x, nueva_y)

            if sobrevive:
                obj_matriz.tablero[self.x][self.y] = "."
                self.x, self.y = nueva_x, nueva_y
                obj_matriz.tablero[self.x][self.y] = "H"
                return True
            else:
                obj_matriz.tablero[self.x][self.y] = "."
                return "MUERTO"
        return True

class salida(piso):
    def colocar(self, matriz_objeto):
        matriz_objeto.tablero[matriz_objeto.fila-1][matriz_objeto.columna-1] = "[]"
        if matriz_objeto.fila > 1 and matriz_objeto.columna > 9:
            matriz_objeto.tablero[1][9] = "{}"
    
    def comprobar(self, obj_matriz, obj_personaje):
        if obj_personaje.x == obj_matriz.fila-1 and obj_personaje.y == obj_matriz.columna-1:
            print("\n¡ENCONTRASTE TU CAMINO!lograste comprender que el camino es mas importante que la meta")
            return False
        elif obj_personaje.x == 1 and obj_personaje.y == 9:
            print("\n¡ENCONTRASTE UNA SALIDA! pero a que costo te volviste un barco a la deriva")
            return False
        return True
