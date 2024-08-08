from clase_padre import Calculo

class CalculadoraConHistorial(Calculo):
    def __init__(self):
        super().__init__()
        self.historial = []
        self.resultado_anterior = None
        

    def realizar_operacion(self, operacion, num1, num2):

        ## Tener en cuenta para usar el método realizar_operacion():
        # las operaciones válidas son 'suma', 'resta', 'multiplicacion' y 'division'
        # num1 y num2 pueden ser numeros o 'ANS'

        # Verificar si los nums son 'ANS'
        if num1 == 'ANS':
            try:
                num1 = self.resultado_anterior
            except (TypeError, ValueError):
                return "Error: num(s) inválido(s)"
            
        if num2 == "ANS":
            try:
                num2 = self.resultado_anterior
            except (TypeError, ValueError):
                return "Error: num(s) inválido(s)"


            
        # Verificar si los nums son válidos
        try:
            result = num1 + num2
        except (TypeError, ValueError):
            return "Error: num(s) inválido(s)"

        # Cargo los atributos de la clase padre
        self.num1 = num1
        self.num2 = num2
        resultado = None

        if operacion == 'suma':
            resultado = Calculo.suma(self) ##usa el metodo suma() de la clase padre

        elif operacion == 'resta':
            resultado = Calculo.resta(self) ##usa el metodo resta() de la clase padre##

        elif operacion == 'multiplicacion':
            resultado = Calculo.multiplicacion(self) ##usa el metodo multiplicacion() de la clase padre##

        elif operacion == 'division':   
            resultado = Calculo.division(self) ##usa el metodo division() de la clase

        else:
            resultado = "Operación no válida"

        self.historial.append((operacion, num1, num2, resultado))
        self.resultado_anterior = resultado

        return resultado

    def mostrar_historial(self):
        for operacion in self.historial:
            print(f"{operacion[1]} {operacion[0]} {operacion[2]} = {operacion[3]}")

