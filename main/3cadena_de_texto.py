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
resultado_separador = separador.join(lista_strings)
print(resultado_separador)