from faker import Faker
import random



dominios_correos = ["gmail.com", "hotmail.com", "yahoo.com", "outlook.com"]

#COSTRUCTOR DE FAKER MIKE
fake = Faker()

#Los ... se llaman elipses y sirven para no maracar error tipo pass

def get_universo_mike(n_people: int = 5):
    for _ in range(n_people):
        name = fake.name()
        print(f"persona{name}con email {name.replace(" ","")}@{random.choice(dominios_correos)}")
    
    return n_people


get_universo_mike(100)