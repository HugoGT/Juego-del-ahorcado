from archives import write
from time import sleep
import random
import os


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
    print("""
    Hola
    Hola""")


def draw():
    clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    word = give_the_word()
    line = word[0]
    letters = word[1]
    list_of_letters = []
    for letter in letters:
        list_of_letters.append(letter)
    guessed_word = ""
    while True:
        clear_console()
        print(welcome())
        option = int(input("\n                                      "))
        if option == 1:
            break
        elif option == 2:
            instructions()
            break
    for i in range(0,4):
        # clear_console()
        print(line)
        print(letters)
        print(list(list_of_letters), "\n")


def run():
    draw()


if __name__ == "__main__":
    run()