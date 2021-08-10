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
    spaces_to_draw = len(word_to_guess)
    line = []
    for i in range(0, spaces_to_draw):
        line.append("_")
    for j in range(0, spaces_to_draw):
        print(line[j])
    print(spaces_to_draw)


def run():
    read()


if __name__ == "__main__":
    run()