"""
    Operadores aritméticos
    Los operadores aritméticos se utilizan para realizar operaciones matemáticas (suma, resta, multiplicación,…).
    La tabla siguiente contiene todos los operadores aritméticos permitidos por Python:
    Operador Ejemplo Significado
    +   a + b Suma
    -   a - b Resta
    -   -a Negación (asignar valor negativo)
    *   a * b Multiplicación
    /   a / b División
    %   a % b Módulo (resto de la división)
    // a // b División entera
    ** a ** b Exponente
"""

"""
    Operadores relacionales o de comparacion
    Los operadores relacionales se utilizan para comparar valores y devuelven como resultado un
    booleano: True o False.

    Operador Ejemplo Significado
    > a > b Mayor que: True si a es mayor que b
    < a > b Menor que: True si a es menor que b
    == a == b Igual: True si a y b son iguales
    != a != b Distinto: True si a y b son distintos
    >= a >= b Mayor o igual: True si a es igual o mayor que b
    <= a >= b Menor o igual: True si a es igual o menor que b

    Operadores lógicos
    Los operadores lógicos and or, y not evalúan valores devolviendo también Trueo False como
    resultado:
    Operador Ejemplo Significado
    and a and b True si a y b son True
    or a or b True si a o b son true
    not not b True si b es falso
"""

def ejercicio_uno():
    try:
        """
        Ejercicio 1
        Crea un programa que solicite al usuario un número del 1 al 10 y muestre por pantalla la tabla de
        multiplicación del 1 al 10.
        Ejemplo:
        1 Introduce un número del 1 al 10: 3
        2 3 x 1 = 3
        3 3 x 2 = 6
        4 3 x 3 = 9
        5 3 x 4 = 12
        6 3 x 5 = 15
        7 3 x 6 = 18
        8 3 x 7 = 21
        9 3 x 8 = 24
        10 3 x 9 = 27
        11 3 x 10 = 30
        """

        leer_numero = int(input("Introduce un numero del 1 al 10: "))
        if 1 <= leer_numero <= 10:
            for i in range(1,11):
                resultado_multiplizaciion = leer_numero*i
                print(f"{leer_numero} x {i} = {resultado_multiplizaciion}")

        else:
            print("El numero no esta dentro del rango solicitado")




    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Fin del programa")

def ejercicio_dos():
    try:
        """
        Ejercicio 2
        Crea un programa que solicite al usuario dos números enteros y muestre por pantalla el resultado
        de las siguientes operaciones: suma, resta, multiplicación y división.
        Ejemplo:
        1 Introduce el primer número: 8
        2 Introduce el segundo número: 2
        3 La suma es: 10
        4 La resta es: 6
        5 La multiplicación es: 16
        6 La división es: 4.0
        """
        leer_numero_a = int(input("Introduce el primer numero: "))
        leer_numero_b = int(input("Introduce el segundo numero: "))
        resultado_suma = leer_numero_a + leer_numero_b
        resultado_resta = leer_numero_a - leer_numero_b
        resultado_resta = leer_numero_a * leer_numero_b
        resultado_resta = leer_numero_a / leer_numero_b
        print(f"La suma es: {resultado_suma}")
        print(f"La resta es: {resultado_resta}")
        print(f"La multiplicacion es: {resultado_resta}")
        print(f"La division es: {resultado_resta}")


    except Exception as e:
        print(f"Error: error en ejercicio_dos {e}")
    finally:
        print("Fin del programa ejercicio_dos")

def area_circulo(radio:float):
    #Calcula el area del circulo
    area = float(3.14159 * (radio**2))
    return area


def ejercicio_tres():
    try:
        """
        Ejercicio 3
        Crea un programa que solicite al usuario el radio de un círculo y calcule el área.
        Nota: Utiliza 3.14159 como número PI para el cálculo del área.
        Ejemplo:
        1 Introduce el radio: 3
        2 El área es: 28.274309999999996
        """
        leer_radio = int(input("Introduce el radio: "))
        area = area_circulo(float(leer_radio))
        print(f"El area es: {area}")

    except Exception as e:
        print(f"Error: error en ejercicio_tres {e}")
    finally:
        print("Fin del programa ejercicio_tres")

if __name__== "__main__":
    # ejercicio_uno()
    # ejercicio_dos()
    ejercicio_tres()