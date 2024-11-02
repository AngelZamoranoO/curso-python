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
class Demo:
    atributo_estatico=123 #Compartido por todos los obhjetos
    def __init__(self,numero) -> None:  
        self.atributo_instancia=numero #especifico de cada objeto
    
c1 = Demo(459)
c2= Demo(786)

#valor inicial
print(f"C1: Estatico {Demo.atributo_estatico}  / Instancia {c1.atributo_instancia}")
#output: C1: Estatico 123 - Instancia: 456
print(f"C2: Estatico {c2.atributo_estatico} / Instancia {c2.atributo_instancia}")

#asigna un valor al atributo_estatico
Demo.atributo_estatico="Esto es estatico"

print(f"C2: Estatico {c2.atributo_estatico} - Instancia {c2.atributo_instancia}")
#output: C2: Estatico Esto es estatico - Instancia 786   

#variable self hace referencia al objeto actual

class PersonaCuatro:
    def __init__(self,nombrefull,email):
        self.nombrefull= nombrefull
        self.email=email
    
    def  mostrarinfo(self):
        return print(f"{self.nombrefull}, su email es {self.email}")

persona_cuatro = PersonaCuatro("Angel Zamorano Oses","angelzamoranoo@gmail.com")
persona_cuatro.mostrarinfo() # muestra la informaciom completa del metodo con su self interno no es necesario pasarle self
print(persona_cuatro.nombrefull) 
print(persona_cuatro.email)

#PRIVATE y PROTECTED
class PersonaPrivada:
    def __init__(self,nombre:str,edad:int):
        self._nombre= nombre #Atributo protected
        self.__edad= edad #Atributo Private

    def getEdad(self):
        return self.__edad
    def setNombre(self,nombre):
        self._nombre= nombre


persona_privada=PersonaPrivada("Angel Zamorano",38)
print("primera llamada a persona_privada._nombre: "+persona_privada._nombre)
#cambio de la variable persona_privada._nombre

#print(persona_privada.__edad) No puedo acceder a este atributo ya que esta privado de la clase, solo lo ve la clase
print(persona_privada.getEdad())

#Coding time
#ejercicio 1

class Coche:
    kilometro_recorrido: float
    gasolina:float
    def __init__(self, matricula:str, marca: str) -> None:
        self.matricula = matricula
        self.marca=marca
    
    
        
