def main():
    try:
        #Cadena de texto (String)
        frase = """Esto es una frase
        muy larga para 
        poder escribir textos mas largos"""

        #Concatenacion de string
        nombre = "Angel Zamorano"
        saludo ="Hola,"+ " "+ nombre+"\n"
        print(saludo)
        #Manejo de listas
        lista_strings=["hola","como","estas",nombre]
        separador = "-"
        resultado_separador = separador.join(lista_strings) # es de manera alternativa aplicar un join
        print(resultado_separador)
        resultado_separador_dos= ' : '.join(lista_strings)
        print(f"Resultado separador 2 -> {resultado_separador_dos}") # puedo unir un listado de nombres y agregar parametro

        #Segundo metodo
        # Forma de agregar parametros o variable dentro del String, el index es por defecto
        print("Meses: {}, {} y {}".format("Enero", "Febrero", "Marzo"))

        # Es especifica orden indicando en la posicion
        print("Meses: {1}, {0} y {2}".format("Enero", "Febrero", "Marzo"))

        #Especifica el orden agregando clave-valor
        print("Meses: {ene}, {mar} y {feb}".format(ene="Enero", feb="Febrero", mar="Marzo"))


        #Cadenas con la f" " integrar variables en la cadena de string 
        print(f"Aca integro variablaes en la cadena -> {nombre}")

        #conversion de tipos, a la hora de concatenar un string con otros de datos puede ser un problema
        # para concatenar debemos cambiar el tipo de dato a string
        tipo_numero = 39
        tipo_float = 3.14
        tipo_boleano = True
        print(f"tranforma el dato en string -> numero {str(tipo_numero)} / float -> {str(tipo_float)} // boleano -> {tipo_boleano}")

        #Metodos en cadenas de texto
        frase_python = "Aprendiendo a programar en python desde 0 a experto"
        #podemos imprimir con Indice
        print(f"Podemos imprimir por indice ascendente-> {frase_python[0]}, {frase_python[4]}, descendente -> {frase_python[-1]}, {frase_python[-3]}")
        #Podemos imprimir obteniendo un extracto del string, incluye el numero inicial hasta el numero final (sin incluir el numero final) devuelve indices
        print(f"Estracto del sub-string -> {frase_python[1:5]}")



    except Exception as e:
        print(f"error en la funcion main -> {e}")
    finally:
        print("Se termina metodo main")

def ejercicio_uno():
    try:
        """
        Ejercicio 1
        Escribe un programa que contenga las siguientes variables:
        - nombre: tipo string y valor “Michael Jordan”
        - edad: tipo integer y valor 50
        - media_puntos: tipo float y valor 28.5
        - activo: False
        El programa deberá mostrar en pantalla todos los valores.
        """
        nombre:str = "Michael Jordan"
        edad:int = 50
        media_puntos:float = 28.5
        activo:bool = False
        print(f"Nombre: {nombre}, Edad: {edad}, media puntos: {media_puntos}, activo: {activo}")
        
    
    except Exception as e:
        print(f"error en la funcion ejercicio_uno -> {e}")
    finally:
        print("Se termina metodo ejercicio_uno")

def ejercicio_dos():
    try:
        """
        Ejercicio 2
        Escribe un programa que solicite el nombre, DNI y edad, lo almacene en 3 variables distintas y
        muestre por pantalla los valores introducidos.
        """
        nombre_uno:str=input("Ingrese el nombre: ")
        dni_uno:int=int(input("Ingrese el DNI: "))
        edad_uno:int=int(input("Ingrese la edad: "))
        print(f"Nombre: {nombre_uno}, DNI: {str(dni_uno)}, edad: {str(edad_uno)} \n")



    
    except Exception as e:
        print(f"error en la funcion ejercicio_dos -> {e}")
    finally:
        print("Se termina metodo ejercicio_dos")


def ejercicio_tres():
    try:
        """
        Ejercicio 3
        Escribe un programa que genere un string compuesto por los primeros 3 caracteres y los últimos 3
        caracteres de un string introducido por el usuario. Pista: tendrás que utilizar la función len() en la
        obtención de los últimos 3 caracteres.
        • Ejemplo 1: ‘aprendiendo’
        • Resultado 1: ‘aprndo’
        • Ejemplo 2: ‘escribiendo código’
        • Resultado 2: ‘escigo’
        """
        leer_string= str(input("Ingrese string comnpuesto: \n"))
        primero_tres= leer_string[:3]
        ultimos_tres= leer_string[-3:]
        print(f"Resultado: {primero_tres}{ultimos_tres}")

        ultimo_tres_len=leer_string[len(leer_string)-3:len(leer_string)]
        print(f"Resultado aplicando len(): {primero_tres}{ultimo_tres_len}")


    except Exception as e:
        print(f"error en la funcion ejercicio_tres -> {e}")
    finally:
        print("Se termina metodo ejercicio_tres")

def ejercicio_4():
    try:
        """
        Ejercicio 4
        Escribe un programa que solicite al usuario dos números y una frase. El primer número introducido
        se corresponderá a la posición de inicio del substring que deberá mostrar el programa por pantalla.
        El segundo número indicará la longitud de dicho substring.
        • Ejemplo 1: Posicion=4, Longitud=8, Frase=’Desarrollar es mi nueva afición’
        • Resultado 1: “rrollar “
        • Ejemplo 2: Posicion=8, Longitud=11, Frase=’Bienvenido a la clase de programación’
        • Resultado 2: “do a la cla”
        """

        leer_texto = str(input("Ingrese el texto a analizar: "))
        leer_posicion = int(input("Ingrese la posicion del substring: "))
        leer_longitud = int(input("Ingrese la longitud del substring: "))
        if leer_posicion < len(leer_texto): 
            substring = leer_texto[leer_posicion:leer_longitud+leer_posicion]
            if leer_longitud <= len(substring):
                print("Resultado: {}".format(substring))
            else:
                total_carateres_restates= leer_texto[leer_posicion:]
                print("Error: La longitud del substring es mayor que la longitud del texto")
                print(f"Resultado error: longitud es {leer_longitud} , caracter restante a la longitud: {total_carateres_restates}, cantidad: {len(total_carateres_restates)}")
        else:
            print("Error: La posicion del substring es mayor que la longitud del texto")

    
    except Exception as e:
        print(f"error en la funcion ejercicio_4 -> {e}")
    finally:
        print("Se termina metodo ejercicio_4")

def ejercicio_cinco():
    try:
        """
        Ejercicio 5
        Escribe un programa que solicite al usuario una frase. A continuación le solicitará la letra que quiere
        reemplazar y por qué letra deberá reemplazarse. Por último el programa mostrará el número de veces
        que la letra está presente en la frase y el resultado final tras reemplazarla.
        • Ejemplo: ‘Desarrollar es mi nuevo pasatiempos’, ‘a’,’e’
        • Resultado: 4 apariciones. ‘Deserroller es mi nueve pesetiempos’
        """

        leer_frase = str(input("Ingrese la frase: "))
        letra_reemplazar = str(input("Ingrese la letra que desea reemplazar: "))
        letra_remplazar_por = str(input("Ingrese la letra va a reemplazar: "))
        contador_letras = leer_frase.count(letra_reemplazar)
        frase_reemplazada = leer_frase.replace(letra_reemplazar,letra_remplazar_por,-1)
        print(f"Resultado: {contador_letras} apariciones. nueva frase: {frase_reemplazada}")
        
        
    
    except Exception as e:
        print(f"error en la funcion ejercicio_cinco -> {e}")
    finally:
        print("Se termina metodo ejercicio_cinco")

if __name__ == "__main__":

    # main()
    # ejercicio_uno()  # Llamamos a la función ejercicio_uno() para ejecutar
    # ejercicio_dos()  # Llamamos a la función ejercicio_dos() para ejecutar
    # ejercicio_tres() # 
    # ejercicio_4()
    ejercicio_cinco()