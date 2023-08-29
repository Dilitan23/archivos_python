# sintaxis para importar

import random 
import random as r
 
# from random import funcion

def jugar(): 
    opciones= ["piedra","papel","tijera"]#opciones del computador 
    jugador= input("Ingrese una opción (piedra,papel,tijera): ").lower()
    
    if jugador not in opciones: # si la eleccion no esta en las opciones , se lanza un error
        print("Opción no válida") 
    else: oponente= random.choice(opciones)
    print(f"El oponente escogió: {oponente}") 
    
    # situaciones donde gana el jugador
    if (jugador == "piedra" and oponente ==" tijera") or (jugador== "papel" and oponente== "piedra") or (jugador=="tijera" and oponente==" papel"):
        print("Ganaste") 

    #situación donde empatan
    elif (jugador == "piedra" and oponente =="piedra") or (jugador== "papel" and oponente== "papel") or (jugador=="tijera" and oponente=="tijera"):
        print("empate")

    # situación donde el jugador pierde 
    elif (jugador == "piedra" and oponente =="papel") or (jugador== "papel" and oponente== "tijera") or (jugador=="tijera" and oponente==" piedra"):
        print("Perdiste")
if __name__=="__main__": 
    jugar()