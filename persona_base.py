from faker import Faker

get_data = Faker()

class PersonaBase():
    def __init__(self):
        self.nombre = get_data.name()
        self.edad = get_data.random_int(min=18, max=30)

    #DEFINICION DE METHODOS
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
