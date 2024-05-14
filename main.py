from paquete.client import Client

def main():
    # Crear un cliente
    client = Client("Juan", "Pérez", 30, "juan@example.com", "España")
    
    # Imprimir información del cliente
    print("Información del cliente:")
    print(client)
    
    # Actualizar el pais del cliente
    client.update_country("Paris")

    #Crear hobbie de cliente
    client.create_hobbies('Cine')

if __name__ == "__main__":
    main()
