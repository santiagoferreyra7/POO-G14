from Base import tablero   # type: ignore


class partidito(tablero):  


    def __init__(self, FS, CS, meter, ficha1, ficha2, quienjuega, gano, empate):
        super().__init__(FS, CS, meter, gano, empate)
        self.ficha1 = ficha1  
        self.ficha2 = ficha2
        self.quienjuega = quienjuega
    def mostrar(self):
        i = 0
        j = 0


        print("------")


        for i in range(0, 3):
            print(" ", end=" ")


            for j in range(0, 3):
                print("|", end=" ")


               
                if self.meter == 1 or self.meter == 2:
                    if i == self.CS and j == self.FS:
                        if self.meter == 1:
                            print(self.ficha1, end=" ")
                        elif self.meter == 2:
                            print(self.ficha2, end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    print(" ", end=" ")


            print("|", end="\n")
            print("------")