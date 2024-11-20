from piedra import Juego
import getpass
# Clase para jugar entre pibes
class JuegoConPibe(Juego):
    def __init__(self):
        super().__init__()

    def jugar(self):
        self.mostrar_reglas()
        try:
            movimiento_jugador1_input = getpass.getpass("Pibe 1, elige: 'z' para Piedra, 'x' para Papel, 'c' para Tijera: ").lower()
            if movimiento_jugador1_input == 'z':
                movimiento_jugador1 = 'Piedra'
            elif movimiento_jugador1_input == 'x':
                movimiento_jugador1 = 'Papel'
            elif movimiento_jugador1_input == 'c':
                movimiento_jugador1 = 'Tijera'
            else:
                raise ValueError("No se puede hacer eso")

            movimiento_jugador2_input = getpass.getpass("Pibe 2, elige: '1' para Piedra, '2' para Papel, '3' para Tijera: ")
            if movimiento_jugador2_input == '1':
                movimiento_jugador2 = 'Piedra'
            elif movimiento_jugador2_input == '2':
                movimiento_jugador2 = 'Papel'
            elif movimiento_jugador2_input == '3':
                movimiento_jugador2 = 'Tijera'
            else:
                raise ValueError("No se puede hacer eso")

            print("\nPibe 1 eligió:", movimiento_jugador1)
            print("Pibe 2 eligió:", movimiento_jugador2)
            resultado = self.determinar_ganador(movimiento_jugador1, movimiento_jugador2)
            print(resultado)
        except ValueError as e:
            print(e)

# Función principal para ejecutar el juego
def main():
    print("Bienvenido al Piedra, Papel y Tijera!")
    modo = input("Elegí el modo de juego: 'compu' para jugar contra la compu, 'pibe' para jugar contra otro pibe: ").lower()
    
    try:
        if modo == 'compu':
            juego = JuegoConCompu()
            juego.jugar()
        elif modo == 'pibe':
            juego = JuegoConPibe()
            juego.jugar()
        else:
            raise ValueError("Opción no válida. Por favor, elige 'compu' o 'pibe'.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
