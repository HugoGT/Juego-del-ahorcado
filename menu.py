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
- Depende de la dificultad el jugador tendrá de 9 a 5 intentos.

Juego:
- En su turno el jugador puede elegir una letra. 
- El computador revisa si la letra pedida se encuentra en la palabra secreta.
-- Si la letra está, entonces el computador la anota sobre la línea que ocupa su lugar en la palabra secreta.
-- Si la letra no está, entonces el jugador perderá una vida.


Fin de la partida:
- GANA el adivinador si descubre la palabra secreta. 
- GANA el computador si el adivinador pierde las 10 vidas antes de adivinar la palabra.

""")


def difficulty():
    dif = input("""Escoja una dificultad para el juego:
    
  1 = Fácil   -> 9 vidas
  2 = Media   -> 7 vidas
  3 = Difícil -> 5 vidas

Ingrese un número: """)

    while type(dif) != int:
        print(dif, type(dif))
        if dif == "1":
            dif = int(dif)
        elif dif == "2":
            dif = int(dif)
        elif dif == "3":
            dif = int(dif)
        else:
            print("\nEscoja entre 1, 2 o 3")
            dif = input("Ingrese un número: ")
    if dif == 1:
        return 1
    elif dif == 2:
        return 2
    else:
        return 3


def win():
    # clear_cls()
    p = """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░█░█n█n█░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░█░██u██░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█████░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░███░███░█░░░███░███░███░██░░░█░░██░░███░███░░░░
░░░░█░░░█░░░█░░░░█░░█░░░░█░░█░█░█░█░█░█░█░░░█░░░░░░
░░░░██░░██░░█░░░░█░░█░░░░█░░█░█░█░█░█░█░██░░███░░░░
░░░░█░░░█░░░█░░░░█░░█░░░░█░░█░█░███░█░█░█░░░░░█░░░░
░░░░█░░░███░███░███░███░███░██░░█░█░██░░███░███░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░███░░█░░█░█░░█░░███░███░███░░░░░░░░░░░░
░░░░░░░░░░░░█░░░█░█░█▌█░█░█░█░░░░█░░█░░░░░░░░░░░░░░
░░░░░░░░░░░░█░░░█░█░███░█░█░███░░█░░██░░░░░░░░░░░░░
░░░░░░░░░░░░█░█░███░█▐█░███░░░█░░█░░█░░░░░░░░░░░░░░
░░░░░░░░░░░░███░█░█░█░█░█░█░███░░█░░███░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

"""
    return p


def loss():
    # clear_cls()
    p = """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█X█X█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░█░░░███░░░███░███░███░█░█░███░███░░░░░░░░░
░░░░░░░░░█░░░█░█░░░█░░░░█░░█░░░█▌█░░█░░█░█░░░░░░░░░
░░░░░░░░░█░░░█░█░░░███░░█░░██░░███░░█░░█░█░░░░░░░░░
░░░░░░░░░█░░░█░█░░░░░█░░█░░█░░░█▐█░░█░░█░█░░░░░░░░░
░░░░░░░░░███░███░░░███░███░███░█░█░░█░░███░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░███░███░███░██░░███░███░███░███░░░░░░░░░░
░░░░░░░░░░█░█░█░░░█░█░█░█░░█░░█░░░░█░░█░░░░░░░░░░░░
░░░░░░░░░░███░██░░██░░█░█░░█░░███░░█░░██░░░░░░░░░░░
░░░░░░░░░░█░░░█░░░█░█░█░█░░█░░░░█░░█░░█░░░░░░░░░░░░
░░░░░░░░░░█░░░███░█░█░██░░███░███░░█░░███░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
    return p


ahorcado = ["""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║═══║░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║░░░║░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░║░░░║░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█o█o█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█o█o█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█o█o█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█o█o█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█o█o█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""",
"""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█████████████████░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░║░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█0█0█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░═════░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█████░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░█░░░█░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░███░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░█░█░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░█░░█░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░█░░░█░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░█░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░█░░░░░░░░░░
░░░░░░░░░█████████████████████████████████░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"""]