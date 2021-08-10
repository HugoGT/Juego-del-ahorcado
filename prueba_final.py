from archives import write
import random

def randomize(numerated_data):
    palabra_random = random.randint(1, 172)
    for palabra in numerated_data:
        if palabra_random == palabra[0]:
            return palabra[1].replace("\n","")


def read():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))
    numerated_data = enumerate(data, 1)
    word_to_guess = randomize(numerated_data)
    print(word_to_guess)
    print(len(word_to_guess))


def run():
    read()


if __name__ == "__main__":
    run()