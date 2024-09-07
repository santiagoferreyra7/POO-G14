from Pibe import partidito as P   # type: ignore

FS = 1
CS = 1
FSA = 5
CSA = 5
meter = 0  
elige = ""
gano = False
igualado = False  

print("Elegí qué tipo de fichas querés para jugar \n")
print("Elegí escribiendo Pr para predeterminadas o Pe para personalizadas \n")
print("Predeterminadas: Jugador 1: X y Jugador 2: O \n")
print("Las fichas personalizadas no pueden tener más de 1 carácter \n")

while elige != "Pr" and elige != "Pe":


    elige = input(str("¿Querés fichas predeterminadas o personalizadas? \n"))


    if elige != "Pr" and elige != "Pe":
        print("Elegí una opción válida \n")


if elige == "Pr":
    ficha1 = "X"  
    ficha2 = "O"  
else:
    ficha1 = input(str("Elegí el carácter deseado para el jugador 1: \n"))


    while len(ficha1) > 1 or len(ficha1) < 1:
        if len(ficha1) > 1 or len(ficha1) < 1:
            print("Elegí una opción válida \n")


            ficha1 = input(str("Elegí el carácter deseado para el jugador 1: \n"))


    ficha2 = input(str("Elegí el carácter deseado para el jugador 2: \n"))


    while len(ficha2) > 1 or len(ficha2) < 1:
        if len(ficha2) > 1 or len(ficha2) < 1:
            print("Elegí una opción válida \n")


            ficha2 = input(str("Elegí el carácter deseado para el jugador 2: \n"))


quienjuega = True  


Participantes = P(FS, CS, meter, ficha1, ficha2, quienjuega, gano, igualado)  
Participantes.mostrar()  
print("\n")


while gano == False or igualado == False:
    Participantes = P(FS, CS, meter, ficha1, ficha2, quienjuega, gano, igualado)


    if quienjuega == True:
        print("Turno del Jugador 1 \n")


        meter = 1
        valido = False


        while not valido:
            FS = int(input("Seleccioná la Fila deseada: \n"))
            FS = FS - 1


            if FS < 0 or FS > 2:
                while FS < 0 or FS > 2:
                    FS = int(input("Seleccioná una posición válida \n"))


                    FS = FS - 1


            CS = int(input("Seleccioná la Columna deseada: \n"))


            CS = CS - 1


            if CS < 0 or CS > 2:
                while CS < 0 or CS > 2:
                    CS = int(input("Seleccioná una posición válida \n"))


                    CS = CS - 1


            if FS == FSA and CS == CSA:
                print("El valor ingresado ya está seleccionado \n")
                valido = False
            else:
                valido = True


            CSA = CS  
            FSA = FS  
    else:
        print("Turno del Jugador 2 \n")


        meter = 2
        valido = False


        while not valido:
            FS = int(input("Seleccioná la Fila deseada: \n"))


            FS = FS - 1


            if FS < 0 or FS > 2:
                while FS < 0 or FS > 2:
                    FS = int(input("Seleccioná una posición válida \n"))


                    FS = FS - 1


            CS = int(input("Seleccioná la Columna deseada: \n"))


            CS = CS - 1


            if CS < 0 or CS > 2:
                while CS < 0 or CS > 2:
                    CS = int(input("Seleccioná una posición válida \n"))


                    CS = CS - 1


            if FS == FSA and CS == CSA:
                print("El valor ingresado ya está seleccionado \n")


                valido = False
            else:
                valido = True


            CSA = CS
            FSA = FS


    Participantes = P(FS, CS, meter, ficha1, ficha2, quienjuega, gano, igualado)

    Participantes.mostrar()

    print("\n")

    quienjuega = not quienjuega  
