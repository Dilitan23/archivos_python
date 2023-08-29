def registrar():
    usuario = "Dilan"
    contraseña = "18-12-22"

# Solicitamos los datos de manera dinámica

    nombre_usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

# Condicion para ingresar

    if usuario == nombre_usuario and contraseña == password: 
        print("La contraseña es correcta puede ingresar")
        return True
    else:
        print("La contraseña es incorrecta porfavor intente denuevo")
        return False
if __name__ == "__main__":
    registrar()