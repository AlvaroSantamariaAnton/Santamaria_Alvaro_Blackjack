# Juego de Blackjack
## Descripción
Este programa implementa un juego simple de Blackjack en la consola. El Blackjack es un juego de cartas en el que el jugador compite contra el crupier para obtener una mano con un valor cercano a 21 sin pasarse. El programa utiliza un diccionario para representar las cartas y sus valores.
## Estructura del código
El código está organizado en funciones, cada una con un propósito específico para facilitar la lectura y el mantenimiento del código.
### Funciones de inicialización y utilidades:
* limpiar_terminal(): limpia la pantalla de la consola.
* obtener_carta(): devuelve una carta aleatoria de la baraja.
### Funciones principales del juego:
* jugar_partida(): gestiona el desarrollo de una partida.
* turno_crupier(): simula el turno del crupier.
* comparacion(): compara las puntuaciones y determina al ganador.
### Función principal del juego (main):
* Se ejecuta en un bucle principal que permite al jugador jugar múltiples partidas y decide si quiere continuar o salir después de cada partida.
## Librerías utilizadas:
* random: permite trabajar con números aleatorios, utilizado aquí para "barajar" la baraja y obtener cartas al azar.
* os: utilizado para limpiar la pantalla de la consola.
* time: permite incorporar pausas en la ejecución del programa, utilizado para dar un aspecto más realista a la interacción con el juego.
## Cómo jugar
1. Al iniciar el juego, se muestra el título "BLACKJACK".
2. Se reparten las cartas al jugador y al crupier.
3. El jugador decide si pedir una carta (p) o plantarse (pl).
4. El juego verifica si el jugador tiene Blackjack, se pasa de 21 o decide plantarse.
5. Si el jugador no se ha pasado de 21, el crupier juega su turno automáticamente.
6. Se comparan las puntuaciones y se determina al ganador.
7. El jugador decide si desea jugar otra vez.
## Ejecución del programa
Ejecuta el script en tu entorno de Python para comenzar a jugar al Blackjack. Sigue las instrucciones en la consola y disfruta del juego.