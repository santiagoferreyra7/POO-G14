from piedra import Juego
import random
# Clase para jugar contra la compu
class JuegoConCompu(Juego):
    def __init__(self):
        super().__init__()

    def jugar(self):
        self.mostrar_reglas()
        try:
            movimiento_jugador = input("Elige: Piedra, Papel o Tijera: ").capitalize()
            if movimiento_jugador not in self.movimientos:
                raise ValueError("No se puede hacer eso")
            
            movimiento_compu = random.choice(self.movimientos)
            print(f"La compu elige: {movimiento_compu}")
            
            resultado = self.determinar_ganador(movimiento_jugador, movimiento_compu)
            print(resultado)
        except ValueError as e:
            print(e)
