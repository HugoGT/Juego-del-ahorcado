from archives import write
from msvcrt import getch
from time import sleep
import menu
import random
import os


def clear_cls():
    clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clear_console()


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
    palabra_random = random.randint(1, 172)
    for palabra in numerated_data:
        if palabra_random == palabra[0]:
            word = palabra[1]
            word = normalize(word)
            return word.replace("\n","")


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
        line += "¯" #line = line + "_"
    with open("./words.txt", "a", encoding="utf-8") as f:
        f.write(word_to_guess)
        f.write("\n")
    return line, word_to_guess


def draw():
    clear_cls()
    print(menu.welcome())
    while True:
        is_num = False
        while is_num == False:
            option = input("\n                                      ")
            if option.isnumeric():
                option = int(option)
                is_num = True
            else:
                print("Escribe una opción correcta")
        if option == 1:
            break
        elif option == 2:
            while True:
                menu.instructions()
                print("Presione cualquier tecla para continuar")
                getch()
                break
            break
        elif option == 3:
            exit()
        else:
            print("Escribe una opción correcta")
    difficulty = menu.difficulty()
    clear_cls()
    return  difficulty


def game():
    word = give_the_word()
    line = word[0]
    word_to_guess = word[1]
    list_of_letters = []
    guessed_word = []
    f_range = len(line)
    f_range = int(f_range)
    difficulty = draw()
    letters_used = []
    avance = False

    if difficulty == 1:
        lives = 9
    elif difficulty == 2:
        lives = 7
    else:
        lives = 5

    for letter in word_to_guess:
        list_of_letters.append(letter)
    for s in line:
        guessed_word.append(" ")

    script = ""
    counter = 15
    for l in line*2:
        if counter %2:
            script += l
        else:
            script += " "
        counter -= 1

    while lives > 0 and lives <= 10:
        clear_cls()
        print(menu.ahorcado(difficulty, avance))
        print(f"Vidas = {lives}", "\n")
        print(f"Letras usadas = {letters_used}\n")
        for i in range(0, int(len(line))):
            print("", guessed_word[i], end= "") 
        print("\n", script, "\n")
        user_input = input(" Ingrese una letra en minúscula: ")
        while True:
            if user_input.islower() and len(user_input) < 2:
                break
            else:
                print(" \n Solo se puede ingresar una letra y que sea minúscula\n")
                user_input = input(" Ingrese una letra: ")
        letters_used.append(user_input)

        sc = 0
        for i in range(0, f_range):
            for j in word_to_guess:
                if j == user_input and word_to_guess[i] == user_input:
                    guessed_word[i] = user_input
                    sc = 1

        if guessed_word == list_of_letters:
            lives += 10
        elif sc == 1:
            lives = lives
        else:
            lives -= 1

    if lives == 0:
        clear_cls()
        print(menu.loss())
        print(f"La palabra era: {word_to_guess}")
    elif lives >= 10:
        clear_cls()
        print(menu.win())
        print(f"La palabra era: {word_to_guess}")
    else:
        print(ValueError)


def run():
    game()


if __name__ == "__main__":
    run()