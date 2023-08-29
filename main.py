import login
import cachipun

def principal():
    print("Bienvenidos al juego de cachipun ")

    if login.registrar() == True:
        cachipun.jugar()

    else:
        print("Vuelve a ingresar")

principal()