# ttateti111.py

class Tablero:
    def __init__(self, FS, CS, colocar, ganar, empate):
        self.FS = FS
        self.CS = CS
        self.colocar = colocar
        self.ganar = ganar
        self.empate = empate

    # Podés agregar otros métodos y atributos acá si hace falta

# juego.py

from ttateti111 import Tablero

class Juego(Tablero):
    def __init__(self, FS, CS, colocar, F1, F2, turno, ganar, empate):
        super().__init__(FS, CS, colocar, ganar, empate)
        self.F1 = F1
        self.F2 = F2
        self.turno = turno

    def imprimir_tablero(self):
        print("  -------------")
        
        for fila in range(3):
            print(" ", end="")
            for columna in range(3):
                print("|", end=" ")
                
                if self.colocar in (1, 2):
                    if fila == self.CS and columna == self.FS:
                        if self.colocar == 1:
                            print(self.F1, end=" ")
                        elif self.colocar == 2:
                            print(self.F2, end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")
            
            print("|")
            print("  -------------")

