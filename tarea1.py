import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]
    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    
    while True:
        # Entrada del jugador
        jugador = input("Elige piedra, papel o tijera (o escribe 'salir' para terminar): ").lower()
        if jugador == "salir":
            print("¡Gracias por jugar!")
            break

        if jugador not in opciones:
            print("Opción inválida. Intenta de nuevo.")
        
    print("Opción inválida. Intenta de nuevo.")
        
    print("Opción inválida. Intenta de nuevo.")
    print("Opción inválida. Intenta de nuevo.")
        











