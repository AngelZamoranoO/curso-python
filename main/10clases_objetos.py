#CLASES Y OBJETOS

class Persona:
    #atributos
    nombre="Angel"
    apellido="Zamorano"
    edad=38

    #metodos
    def camina(self):
        print(self.nombre," camina por la calle")

p1 = Persona()
print("Nombre de persona 1: ", p1.nombre)
print("Apellido de persona 1: ", p1.apellido)
p1.camina()
#-----------------------------------------------    


#clase con metodo constructor
class PersonaDos:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def saludar(self):
        print("Hola, soy", self.nombre, "y tengo", self.edad, "años.")

persona2 = PersonaDos("Ana", "García", 25)
print("Nombre de persona 2: ", persona2.nombre)
print("Apellido de persona 2: ", persona2.apellido)
persona2.saludar()
#-----------------------------------------------

#clases con atributo de clase vs atributos de instancias


        