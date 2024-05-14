
class Client:
    def __init__(self, name, last_name, age, email, country):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.email = email
        self.country = country
    
    def __str__(self):
        return f"Cliente: {self.name} {self.last_name}, Edad: {self.age}, Correo: {self.email}, Pais: {self.country}"
    
    def update_country(self, new_country):
        self.country = new_country
        print(f"El lugar de residencia del cliente {self.name} {self.last_name} se ha sido actualizado a: {self.country}")
    
    def create_hobbies(self, hobbie):
        self.hobbies = hobbie
        print(f"El cliente creo el siguiente hobbie de interes: {self.hobbies}")


