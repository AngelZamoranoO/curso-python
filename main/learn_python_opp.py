"""
Learn Python OOP in under 20 Minutes
url:
https://www.youtube.com/watch?v=rLyYb7BFgQI

"""

class Microwave:
    #Inicializador
    def __init__(self, brand:str, power_rating:str) -> None:
        #se inicializa con las variables locales de la clase
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False
    
    #Metodos
    def turn_on(self) -> None:
        if self.turn_on:
            print(f"El microondas {self.brand} ya esta encendido")
        else:
            self.turn_on= True
            print(f"El microondas {self.brand} esta encendido")


    def turn_off(self) -> None:
        if self.turned_on_on:
            self.turned_on = False
            print(f"El microondas {self.brand} ya ahora apagado")
        else:
            print(f"El microondas {self.brand} ya esta apagado")

    def run(self, seconds: int):
        if self.turned_on:

            print(f"Corriendo ({self.brand}) por {seconds} seconds")
        else:
            print(f"El mistica fuerza del deseo: 'Enciende tu microondas primero'")

smeg: Microwave = Microwave("Smeg", "B") #INSTANCIA ESTA CLASE QUE ES UN OBJETO UNICO
smeg.turn_on()
smeg.turn_on()

bosh:Microwave = Microwave("Bosh", )

