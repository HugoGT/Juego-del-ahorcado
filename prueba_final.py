from time import sleep
from msvcrt import getch
import random
import os


def clear_cls():    
    clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear_console()


def give_the_word():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))
    numerated_data = enumerate(data, 1)
    word_to_guess = randomize(numerated_data)
    spaces_to_draw = len(word_to_guess)
    line = ""
    for i in range(0, spaces_to_draw):
        line += "_ "
    return line, word_to_guess


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s


def randomize(numerated_data):
    palabra_random = random.randint(2, 2)
    for palabra in numerated_data:
        if palabra_random == palabra[0]:
            word = palabra[1]
            word = normalize(word)
            return word.replace("\n","")


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


def draw():
    clear_cls()
    while True:
        print(welcome())
        option = int(input("\n                                      "))
        if option == 1:
            break
        elif option == 2:
            while True:
                instructions()
                print("Presione cualquier tecla para continuar")
                getch()
                break
            break
        elif option == 3:
            exit()
        else:
            print("Escribe una opción correcta")
            sleep(2)


def game():
    word = give_the_word()
    line = word[0]
    letters = word[1]
    list_of_letters = []
    for letter in letters:
        list_of_letters.append(letter)
    guessed_word = ""
    for i in range(0,4):
        # clear_console()
        print(line)
        print(letters)
        print(list(list_of_letters), "\n")
        break


def run():
    draw()
    game()


if __name__ == "__main__":
    run()