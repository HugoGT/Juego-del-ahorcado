from msvcrt import getch
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
    palabra_random = random.randint(2, 2)
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
        line += "_"
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
    clear_cls()


def game():
    lives = 2
    word = give_the_word()
    line = word[0]
    letters = word[1]
    list_of_letters = []
    guessed_word = []
    for letter in letters:
        list_of_letters.append(letter)
    for sub_script in line:
        guessed_word.append(sub_script)
    script = ""
    counter = 15
    for l in line*2:
        if counter %2:
            script += l
        else:
            script += " "
        counter -= 1
    line = script
    while lives > 0 and lives <= 10:
        clear_cls()
        print("\n", line, "\n")
        user_input = input(" Ingrese una letra en minúscula: ")
        while True:
            if user_input.islower() and len(user_input) < 2:
                break
            else:
                print(" \n Solo se puede ingresar una letra y que sea minúscula\n")
                user_input = input(" Ingrese una letra: ")
        print(letters, "\n")
        print(list_of_letters)
        print(guessed_word)
        lives -= 1
        if guessed_word == list_of_letters:
            lives += 10


def run():
    draw()
    game()


if __name__ == "__main__":
    run()