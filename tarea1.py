import random

def obtener_opcion_usuario():
    """Solicita al usuario que elija piedra, papel o tijera."""
    opciones = ['piedra', 'papel', 'tijera']
    while True:
        usuario = input("Elige piedra, papel o tijera: ").lower()  # Normalizamos a minúsculas para evitar errores.
        if usuario in opciones:  # Verificamos que sea una opción válida.
            return usuario
        else:
            print("Opción no válida. Intenta de nuevo.")

def obtener_opcion_computadora():
    """Devuelve una opción aleatoria para la computadora."""
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)  # Selecciona una opción al azar.

def determinar_ganador(usuario, computadora):
    """Determina el ganador entre el usuario y la computadora."""
    if usuario == computadora:
        return "empate"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        return "usuario"
    else:
        return "computadora"

def main():
    """Función principal para ejecutar el juego."""
    print("\n¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("El objetivo es ganar tantas rondas como puedas. ¡Buena suerte!")

    victorias = 0  # Contador de victorias del usuario.
    derrotas = 0   # Contador de derrotas del usuario.

    while True:
        print("\n--- Nueva Ronda ---")

        # Obtener las opciones del usuario y de la computadora.
        usuario = obtener_opcion_usuario()
        computadora = obtener_opcion_computadora()

        # Mostrar las elecciones.
        print(f"\nElegiste: {usuario}")
        print(f"La computadora eligió: {computadora}")

        # Determinar el resultado de la ronda.
        resultado = determinar_ganador(usuario, computadora)

        if resultado == "empate":
            print("\n¡Es un empate!")
        elif resultado == "usuario":
            print("\n¡Ganaste esta ronda!")
            victorias += 1  # Incrementar victorias del usuario.
        else:
            print("\n¡Perdiste esta ronda!")
            derrotas += 1  # Incrementar derrotas del usuario.

        # Mostrar el marcador actual.
        print(f"\nMarcador actual: Victorias = {victorias}, Derrotas = {derrotas}")

        # Preguntar si el usuario quiere jugar otra ronda.
        jugar_otra = input("\n¿Quieres jugar otra ronda? (sí/no): ").lower()
        if jugar_otra != "sí":
            break  # Salir del bucle si el usuario no quiere continuar.

    # Finalizar el juego y mostrar resultados finales.
    print("\n--- Juego Terminado ---")
    print(f"Resultados finales: Victorias = {victorias}, Derrotas = {derrotas}")
    if victorias > derrotas:
        print("\n¡Felicidades! Eres el ganador del juego.")
    elif victorias < derrotas:
        print("\nLamentablemente perdiste el juego. ¡Intenta de nuevo!")
    else:
        print("\nEl juego terminó en empate. ¡Buen esfuerzo!")

if __name__ == "__main__":
    main()








