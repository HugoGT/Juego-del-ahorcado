import os


def clear_cls():    
    clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear_console()


def welcome():
    welcom = """  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░████░█████░████░██░░█░█░░░░░█░████░██░░█░█████░████░░█████░░░░░░░░░
░░░░░░░░█░░█░░░█░░░█░░░░██░░█░██░░░██░█░░░░██░░█░░░█░░░█░░░█░█░░░█░░░░░░░░░
░░░░░░░░████░░░█░░░███░░█░█░█░░██░██░░███░░█░█░█░░░█░░░█░░░█░█░░░█░░░░░░░░░
░░░░░░░░█░░█░░░█░░░█░░░░█░░██░░░███░░░█░░░░█░░██░░░█░░░█░░░█░█░░░█░░░░░░░░░
░░░░░░░░████░█████░████░█░░░█░░░░█░░░░████░█░░░█░█████░████░░█████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░██░░█░░░░░░░░█████░█░░█░████░█████░█████░░░░░████░░████░░░░░░░░░░░
░░░░░░░░█░░█░█░░░░░░░░░░█░░░█░░█░█░░░░█░░░░░█░░░█░░░░░█░░░█░█░░░░░░░░░░░░░░
░░░░░░░░█░░█░█░░░░░░░░░░█░░░█░░█░███░░█░░██░█░░░█░░░░░█░░░█░███░░░░░░░░░░░░
░░░░░░░░████░█░░░░░░░░░░█░░░█░░█░█░░░░█░░░█░█░░░█░░░░░█░░░█░█░░░░░░░░░░░░░░
░░░░░░░░█░░█░████░░░░░███░░░████░████░█████░█████░░░░░████░░████░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░█░█░░████░█░░░░░░░░░░██░░█░░█░████░███░░████░░██░░███░░████░░█░█░░░
░░░░░░░░░░░░░█░░░░█░░░░░░░░░█░░█░█░░█░█░░█░█░░█░█░░░░█░░█░█░░█░█░░█░░░░░░░░
░░░░░░░░░░░░░███░░█░░░░░░░░░█░░█░████░█░░█░███░░█░░░░█░░█░█░░█░█░░█░░░░░░░░
░░░░░░░░░░░░░█░░░░█░░░░░░░░░████░█░░█░█░░█░█░░█░█░░░░████░█░░█░█░░█░░░░░░░░
░░░░░░░░░░░░░████░████░░░░░░█░░█░█░░█░████░█░░█░████░█░░█░███░░████░░░░░░░░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                 1) Jugar
                             2) Instrucciones
                                 3) Salir"""
    return welcom


def instructions():
    clear_cls()
    print("""Objetivo: Descubrir la palabra secreta.

Preparación:
- Al inicio el computador pensará en una palabra o frase y dibujará una línea por cada letra.
- El jugador tiene 10 intentos antes de perder.

Juego:
- En su turno el jugador puede elegir una letra. 
- El computador revisa si la letra pedida se encuentra en la palabra secreta.
-- Si la letra está, entonces el computador la anota sobre la línea que ocupa su lugar en la palabra secreta.
-- Si la letra no está, entonces el jugador perderá una vida.


Fin de la partida:
- GANA el adivinador si descubre la palabra secreta. 
- GANA el computador si el adivinador pierde las 10 vidas antes de adivinar la palabra.

""")

def win():
    p = "Ganaste"
    return p


def loss():
    p = "Perdiste"
    return p