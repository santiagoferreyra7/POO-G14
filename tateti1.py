class tablero:
    def __init__(self, filaseleccionada, columnaseleccionada, meter, gano, igualado):
        self.filaseleccionada = filaseleccionada  
        self.columnaseleccionada = columnaseleccionada
        self.meter = meter
        self.gano = gano  
        self.igualado = igualado  
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]  # Tablero vacío de 3x3

    def colocar_ficha(self, ficha):
        # Coloca la ficha en la posición seleccionada
        self.tablero[self.filaseleccionada][self.columnaseleccionada] = ficha

    def triunfazo(self, ficha):
        # Verifica si hay un ganador
        # Comprobación de filas
        for fila in self.tablero:
            if all(celda == ficha for celda in fila):
                return True
        # Comprobación de columnas
        for col in range(3):
            if all(self.tablero[fila][col] == ficha for fila in range(3)):
                return True
        # Comprobación de diagonales
        if all(self.tablero[i][i] == ficha for i in range(3)):
            return True
        if all(self.tablero[i][2 - i] == ficha for i in range(3)):
            return True
        return False

    def es_empate(self):
        # Verifica si todas las posiciones están llenas y no hay ganador
        for fila in self.tablero:
            if " " in fila:
                return False
        return True
