
db = {
    'Jhon':'12Doe',
    'Juan':'D456',
}

def register_user():
    while True:
        username_input = input('Ingrese su nombre de usuario: ')
        if username_input in db:
            print('Su nombre de usuario ya esta en uso, intente con otro')
        else:
            break

    password_input = input('Ingrese su contraseña: ')
    db[username_input] = password_input
    print('Se registro con exito ', db)


def read_db():
    print(db)

def login_user():
    while True:
        username_input = input('Ingrese su nombre de usuario: ')
        password_input = input('Ingrese su contraseña: ')
        if username_input in db and db[username_input] == password_input:
            print('Sesión iniciada')
            break
        else:
            print('Nombre de usuario o contraseña incorrectos')
