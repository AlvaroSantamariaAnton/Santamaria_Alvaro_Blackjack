"""
JUEGO DE BLACKJACK
------------------

Este programa implementa un juego simple de Blackjack en la consola. 
El Blackjack es un juego de cartas en el que el jugador compite contra 
el crupier para obtener una mano con un valor cercano a 21 sin pasarse. 
El programa utiliza un diccionario para representar las cartas y sus valores.

ESTRUCTURA DEL CÓDIGO
----------------------

El código está organizado en funciones, cada una con un propósito específico 
para facilitar la lectura y el mantenimiento del código.

Funciones de inicialización y utilidades:
- limpiar_terminal(): limpia la pantalla de la consola.
- obtener_carta(): devuelve una carta aleatoria de la baraja.

Funciones principales del juego:
- jugar_partida(): gestiona el desarrollo de una partida.
- turno_crupier(): simula el turno del crupier.
- comparacion(): compara las puntuaciones y determina al ganador.

Función principal del juego (main):
- Se ejecuta en un bucle principal que permite al jugador jugar múltiples 
  partidas y decide si quiere continuar o salir después de cada partida.

LIBRERÍAS UTILIZADAS:
---------------------
- random: permite trabajar con números aleatorios, 
utilizado aquí para "barajar" la baraja y obtener cartas al azar.
- os: utilizado para limpiar la pantalla de la consola.
- time: permite incorporar pausas en la ejecución del programa, 
utilizado para dar un aspecto más realista a la interacción con el juego.
"""

import random
import os
import time

# Definir el diccionario de cartas y sus valores
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 

# Crear una lista de cartas para poder escoger una carta
lista_cartas = list(cartas.keys())

def limpiar_terminal():
    # Función para limpiar la terminal

    os.system('cls' if os.name == 'nt' else 'clear')


# Inicio del juego - "Título"
titulo = "BLACKJACK"
print("\n" + titulo + "\n" + "-" * len(titulo))


def obtener_carta():
    # Función para obtener una carta aleatoria

    carta = random.choice(lista_cartas)
    return carta


def jugar_partida():
    # Función para jugar una partida

    global carta1_crupier, carta2_crupier, puntuacion_crupier, puntuacion_jugador

    time.sleep(0.5)     # Introduce una pausa de x segundos en la ejecución del programa
    print("\nSe barajan las cartas...")
    time.sleep(1)
    print("\nSe reparten las cartas...")

    # Obtiene dos cartas al azar y las suma para la puntuación del jugador
    carta1_jugador = obtener_carta()
    carta2_jugador = obtener_carta()
    puntuacion_jugador = cartas[carta1_jugador] + cartas[carta2_jugador]

    # Imprime las cartas y la puntuación del jugador
    time.sleep(1)
    print(f"\nTu mano es: {carta1_jugador} , {carta2_jugador}")
    mensaje_puntuacion_jugador = f"\nTu puntuación es: {puntuacion_jugador}"
    time.sleep(1)
    print(mensaje_puntuacion_jugador + "\n" + "-" * len(mensaje_puntuacion_jugador))

    # Verificar si las dos primeras cartas suman 21 (Blackjack)
    if puntuacion_jugador == 21:
        time.sleep(1)
        print("\n¡Tienes Blackjack!")

    # Obtiene dos cartas al azar y las suma para la puntuación del crupier
    carta1_crupier = obtener_carta()
    carta2_crupier = obtener_carta()
    puntuacion_crupier = cartas[carta1_crupier] + cartas[carta2_crupier]

    # Imprime las cartas y la puntuación del crupier
    time.sleep(1)
    print(f"\nLa mano del crupier es: {carta1_crupier} , ???")                                                                  
    mensaje_puntuacion_crupier = f"\nLa puntuación del crupier es: {puntuacion_crupier - cartas[carta2_crupier]}"   # Resta el valor de la segunda carta a la puntuación, ya que esta aún está oculta
    time.sleep(1)                                                                                                  
    print(mensaje_puntuacion_crupier + "\n" + "-" * len(mensaje_puntuacion_crupier))

    # Empieza el turno del jugador
    time.sleep(1)
    print("\nTu turno:")

    while True:

        time.sleep(0.5)
        ask_player = str(input("\n¿Quieres pedir una carta (p) o plantarte (pl)?: "))

        if ask_player == "p":
            carta_jugador = obtener_carta()
            time.sleep(0.5)
            print("\nTe reparten una carta...")
            time.sleep(1)
            print(f"\nHas sacado: {carta_jugador}")
            puntuacion_jugador += cartas[carta_jugador]
            time.sleep(1)
            print(f"\nTu puntuación es: {puntuacion_jugador}")

            if puntuacion_jugador == 21:
                time.sleep(1)
                print("\n¡Tienes Blackjack!")
                break
            elif puntuacion_jugador > 21:
                time.sleep(1)
                print("\nTe has pasado de 21, el crupier gana.")
                return None     # Terminar el juego si el jugador se pasa de 21
            else:
                pass

        elif ask_player == "pl":
            time.sleep(1)
            print("\nTe has plantado")
            break
        else:
            print("Por favor, ingresa 'p' para pedir o 'pl' para plantarte.")
    
    return puntuacion_jugador


def turno_crupier():
    # Función para el turno del crupier

    global carta1_crupier, carta2_crupier, puntuacion_crupier

    time.sleep(1)
    print("\nTurno del crupier:")
    time.sleep(0.5)
    print("\nEl crupier desvela su segunda carta...")
    time.sleep(1)
    print(f"\nLa mano del crupier es: {carta1_crupier} , {carta2_crupier}")
    time.sleep(1)
    print(f"\nLa puntuación del crupier es: {puntuacion_crupier}")
    
    while puntuacion_crupier < 17:

        time.sleep(1)
        print("\nEl crupier pide una carta...")
        carta_crupier = obtener_carta()
        time.sleep(1)
        print(f"\nEl crupier ha sacado {carta_crupier}")
        puntuacion_crupier += cartas[carta_crupier]
        time.sleep(1)
        print(f"\nLa puntuación del crupier es: {puntuacion_crupier}")

    if puntuacion_crupier == 21:
        time.sleep(1)
        print("\n¡El crupier tiene Blackjack!")
    elif puntuacion_crupier > 21:
        pass
    else:
        time.sleep(1)
        print("\nEl crupier se planta")

    return puntuacion_crupier


def comparacion():
    # Función para comparar las puntuaciones

    global puntuacion_crupier, puntuacion_jugador

    if puntuacion_crupier > 21:
        time.sleep(1)
        print("\nEl crupier se ha pasado de 21, has ganado.")
    else:
        if puntuacion_jugador == puntuacion_crupier:
            time.sleep(1)
            print("\nTu puntuación es igual que la del crupier, ¡Hay un empate!")
        elif puntuacion_jugador < puntuacion_crupier:
            time.sleep(1)
            print("\nLa puntuación del crupier es mayor, has perdido")
        elif puntuacion_jugador > puntuacion_crupier:
            time.sleep(1)
            print("\nTu puntuación es mayor, has ganado")


def main():
    # Función principal del juego
    while True:
        
        puntuacion_jugador = jugar_partida()

        # Solo ejecutar turno_crupier y comparacion si el juego no ha terminado (si el juagdor no se ha pasado de 21)
        if puntuacion_jugador is not None:
            print("\n" + "-" * 50)
            turno_crupier()
            print("\n" + "-" * 50)
            comparacion()

        while True:

            time.sleep(1)
            play_again = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

            if play_again in ['s', 'n']:
                break
            else:
                print("Por favor, ingresa 's' para jugar otra vez o 'n' para salir.")

        if play_again == 'n':
            print("\nGracias por jugar. ¡Hasta otra!")
            break
        else:
            limpiar_terminal()
            pass

if __name__ == "__main__":
    main()