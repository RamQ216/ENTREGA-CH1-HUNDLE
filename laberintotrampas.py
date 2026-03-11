import random

class Matriz:
    def __init__(self):
        self.fila = int(input("ingrese un numero de filas: "))
        self.columna = int(input("ingrese un numero de columnas: "))
        self.tablero = []

    def crear(self):
        self.tablero = [["." for _ in range(self.columna)] for _ in range(self.fila)]
        return self.tablero
    
    def mostrar(self):
        for i in self.tablero:
            print(" ".join(i))

class piso():
    def interaccion(self, tablero, x, y):
        # Esta es la lógica del 20%
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
        # Esta es la lógica del 50%
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

class personaje():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vidas=3

    def colocar(self, matriz_objeto):
        matriz_objeto.tablero[self.x][self.y] = "H"

    def mover(self, obj_matriz, p_normal, p_lava):
        entrada = input("W:arriba, S:abajo, A:izq, D:derecha, Q=salir: ").upper()
        if entrada == "Q": return "Q"

        nueva_x, nueva_y = self.x, self.y
        if entrada == "W": 
            nueva_x -= 1
        elif entrada == "S": 
            nueva_x += 1
        elif entrada == "A": 
            nueva_y -= 1
        elif entrada == "D": 
            nueva_y += 1

        # Validar límites
        if 0 <= nueva_x < obj_matriz.fila and 0 <= nueva_y < obj_matriz.columna:
            simbolo_destino = obj_matriz.tablero[nueva_x][nueva_y]
            sobrevive = True

            # INTERACCIÓN SEGÚN EL SUELO
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
        # Primera salida: Final del tablero
        matriz_objeto.tablero[matriz_objeto.fila-1][matriz_objeto.columna-1] = "[]"
        
      
        if matriz_objeto.fila > 1 and matriz_objeto.columna > 9:
            matriz_objeto.tablero[1][9] = "{}"
    
    def comprobar(self, obj_matriz, obj_personaje):
        if obj_personaje.x == obj_matriz.fila-1 and obj_personaje.y == obj_matriz.columna-1:
            print("\n¡ENCONTRASTE TU CAMINO! diste fin al ciclo de incertidumbre que tenias en el corazon")
            return False
        
        elif obj_personaje.x == 1 and obj_personaje.y == 9:
            print("\n¡ENCONTRASTE UNA SALIDA! pero a que costo, tus propias acciones te condenaron a ser un barco a la deriva")
            return False
        return True

class JUEGO:
    def __init__(self):
        self.juego = Matriz()
        self.pj = personaje()
        self.piso_normal = piso()
        self.piso_2 = piso_lava()
        self.escape = salida()

    def iniciar(self):
        self.juego.crear()
        self.pj.colocar(self.juego)
        self.piso_normal.colocar(self.juego)
        self.piso_2.colocar(self.juego)
        self.escape.colocar(self.juego)

        while True:
            self.juego.mostrar()
            # Ahora pasamos los pisos al movimiento para que interactúen
            resultado = self.pj.mover(self.juego, self.piso_normal, self.piso_2)
            
            if resultado == "Q":
                break
            if resultado == "MUERTO":
                print(f"MORISTE, TE QUEDAN {self.pj.vidas} VIDAS")
                self.pj.vidas-=1
            if self.pj.vidas==0:
                print("GAME OVER")
            if not self.escape.comprobar(self.juego, self.pj):
                break

# Ejecución
partida = JUEGO()
partida.iniciar()