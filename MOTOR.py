from DOMINIO import personaje,piso,piso_lava,salida
from UICONSOLA import Matriz
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
            resultado = self.pj.mover(self.juego, self.piso_normal, self.piso_2)
            
            if resultado == "Q": break
            if resultado == "MUERTO":
                self.pj.restar_vida() # Usamos el método para modificar el atributo privado
                print(f"MORISTE, TE QUEDAN {self.pj.vidas} VIDAS")
            
            if self.pj.vidas == 0:
                print("GAME OVER")
                break
            if not self.escape.comprobar(self.juego, self.pj):
                break
