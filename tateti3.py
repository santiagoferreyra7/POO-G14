from tateti1 import tablero

class partidito(tablero):  
    def __init__(self, FS, CS, meter, ficha1, ficha2, quienjuega, gano, empate):
        super().__init__(FS, CS, meter, gano, empate)
        self.ficha1 = ficha1  
        self.ficha2 = ficha2
        self.quienjuega = quienjuega

    def mostrar(self):
        print("------")
        for fila in self.tablero:
            print(" ", end=" ")
            for celda in fila:
                print("|", celda, end=" ")
            print("|")
            print("------")
