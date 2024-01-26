# VARIABLES Y TIPOS DE DATOS

nombre = "Angel Zamorano" # cadena de texto

edad = 30 # numero entero
peso = 75.5 #numero decimal o flotante
# Booleano: representa un valor verdadero (True) o falso (False).

# Metodos de cadena de string
print(len(nombre)) # Devuelve la longitud del nombre
print(nombre.upper()) #Devuelve el nombre en mayusculas
print(nombre[1]) # Devuelve el segundo carácter de nombre
print("Hola, " + nombre) # Concatenacion de cadenas

# Metodos de numeros enteros
print(edad//2) # Division Entera
print(edad%2) # Residuo de division
print(-edad) # Numero negativo

#Metodos de numeros decimal
print(round(peso)) # Redondear a numero entero mas cercano
print(int(peso)) # Convertir a entero
print(float(edad)) #Convertir a float
# Operadores aritmeticos
suma= edad+ peso
resta= edad- peso
multiplicacion= edad* peso
division= edad/ peso
potencia= edad**2

print(f"La suma es de {suma} \n la resta es de {resta}\n la multiplicacion es de {multiplicacion}\n la division es de {division}\n la potencia es de {potencia}")

#Lecturas de datos en Python
# entero = int(input("Ingrese un numero: "))
# flotante = float(input("Ingrese numero flotante: "))
# cadena_texto = input("Ingrese una palabra: ")
# booleano = input("True/False:")
# validar_booleano = True if booleano.lower() == "true" else False

# print("El numero es", entero)
# print("La numero decimal es ", flotante)
# print("La palabra es ", cadena_texto)
# print("El valor booleano: ", validar_booleano)


