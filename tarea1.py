import random

def obtener_opcion_usuario():
    """Solicita al usuario que elija piedra, papel o tijera."""
    opciones = ['piedra', 'papel', 'tijera']
    while True:
        usuario = input("Elige piedra, papel o tijera: ").lower()
        if usuario in opciones:
            return usuario
        else:
            print("Opción no válida. Intenta de nuevo.")

def obtener_opcion_computadora():
    """Devuelve una opción aleatoria para la computadora."""
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    """Determina el ganador entre el usuario y la computadora."""
    if usuario == computadora:
        return "¡Es un empate!"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"










