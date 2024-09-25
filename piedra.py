import random
import getpass  # Para ocultar la entrada del jugador

# Clase base que explica el juego
class Juego:
    def __init__(self):
        self.movimientos = ['Piedra', 'Papel', 'Tijera']
        self.reglas = {
            'Piedra': 'Tijera',
            'Papel': 'Piedra',
            'Tijera': 'Papel'
        }
   
    def mostrar_reglas(self):
        print("Reglas del juego:")
        print("Piedra le gana a Tijera")
        print("Tijera le gana a Papel")
        print("Papel le gana a Piedra")


    def determinar_ganador(self, jugador1, jugador2):
        if jugador1 == jugador2:
            return "Empataron"
        elif self.reglas[jugador1] == jugador2:
            return "Jugador 1 ganó"
        else:
            return "Jugador 2 gano"
