from clases import CalculadoraConHistorial


def mostrar_menu():
    print("\nMenú de Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Mostrar Historial")
    print("6. Salir")

def obtener_num(mensaje):
    num = input(mensaje)
    if num.lower() == "ans":
        return "ANS"
    else:
        return int(num)


def main():
    calculadora = CalculadoraConHistorial()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        operacion = ""

        if opcion == "1":
            operacion = "suma"
        elif opcion == "2":
            operacion = "resta"
        elif opcion == "3":
            operacion = "multiplicacion"
        elif opcion == "4":
            operacion = "division"
        
        if opcion == '1':
            num1 = obtener_num("Ingrese el primer número o 'ANS': ")
            num2 = obtener_num("Ingrese el segundo número o 'ANS': ")


            print("\n\nResultado:", calculadora.realizar_operacion(operacion, num1, num2))  # despues de la coma usar el metodo realizar_operacion() del objeto calculadora
                                        # al metodo le tienen que pasar los argumentos que necesita
                                        # prestar atención a los argumentos que corresponden a cada operación

        elif opcion == '2':
            num1 = obtener_num("Ingrese el primer número o 'ANS': ")
            num2 = obtener_num("Ingrese el segundo número o 'ANS': ")

            print("\n\nResultado:",  calculadora.realizar_operacion(operacion, num1, num2))  # despues de la coma usar el metodo realizar_operacion() del objeto calculadora
                                        # al metodo le tienen que pasar los argumentos que necesita
                                        # prestar atención a los argumentos que corresponden a cada operación

        elif opcion == '3':
            num1 = obtener_num("Ingrese el primer número o 'ANS': ")
            num2 = obtener_num("Ingrese el segundo número o 'ANS': ")
            print("\n\nResultado:", calculadora.realizar_operacion(operacion, num1, num2))   # despues de la coma usar el metodo realizar_operacion() del objeto calculadora
                                        # al metodo le tienen que pasar los argumentos que necesita
                                        # prestar atención a los argumentos que corresponden a cada operación

        elif opcion == '4':
            num1 = obtener_num("Ingrese el primer número o 'ANS': ")
            num2 = obtener_num("Ingrese el segundo número o 'ANS': ")
            print("\n\nResultado:", calculadora.realizar_operacion(operacion, num1, num2))   # despues de la coma usar el metodo realizar_operacion() del objeto calculadora
                                        # al metodo le tienen que pasar los argumentos que necesita
                                        # prestar atención a los argumentos que corresponden a cada operación

        elif opcion == '5':
            calculadora.mostrar_historial()
        elif opcion == '6':
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
