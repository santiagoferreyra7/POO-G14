from tateti2 import partidito

FS = 1  # Fila seleccionada
CS = 1  # Columna seleccionada
FSA = 5  # Fila seleccionada anteriormente
CSA = 5  # Columna seleccionada anteriormente
meter = 0  # Indicador de colocar ficha
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
        print("Opción inválida, por favor elegí Pr o Pe \n")

ficha1 = "X" if elige == "Pr" else input("Jugador 1, elegí tu ficha: \n")
ficha2 = "O" if elige == "Pr" else input("Jugador 2, elegí tu ficha: \n")

quienjuega = True  # Empieza el jugador 1

# Crear instancia de 'partidito'
Participantes = partidito(FS, CS, meter, ficha1, ficha2, quienjuega, gano, igualado)

while not gano and not igualado:
    if quienjuega:
        print("Turno del Jugador 1 \n")
        meter = 1
        ficha_actual = ficha1
    else:
        print("Turno del Jugador 2 \n")
        meter = 2
        ficha_actual = ficha2

    valido = False
    while not valido:
        FS = int(input("Seleccioná la Fila deseada (1-3): \n")) - 1
        while FS < 0 or FS > 2:
            FS = int(input("Seleccioná una posición válida (1-3): \n")) - 1

        CS = int(input("Seleccioná la Columna deseada (1-3): \n")) - 1
        while CS < 0 or CS > 2:
            CS = int(input("Seleccioná una posición válida (1-3): \n")) - 1

        if Participantes.tablero[FS][CS] != " ":
            print("La posición ya está ocupada, elegí otra.\n")
            valido = False
        else:
            valido = True
            Participantes.filaseleccionada = FS
            Participantes.columnaseleccionada = CS

    # Colocar ficha y mostrar tablero
    Participantes.colocar_ficha(ficha_actual)
    Participantes.mostrar()
    print("\n")

    # Verificar si hay un ganador o empate
    if Participantes.triunfazo(ficha_actual):
        gano = True
        print(f"¡Jugador {'1' if quienjuega else '2'} ({ficha_actual}) ha ganado!\n")
    elif Participantes.es_empate():
        igualado = True
        print("¡El juego terminó en empate!\n")

    quienjuega = not quienjuega  # Cambia de jugador