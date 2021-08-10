import random

# def randomize(numerated_data):
#     palabra_random = random.randint(1, 172)
#     for palabra in numerated_data:
#         if palabra_random == palabra[0]:
#             return palabra


def read():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))
    numerated_data = enumerate(data, 1)
    print("Return type: ", type(numerated_data))
    palabra_random = random.randint(1, 172)
    for palabra in numerated_data:
        if palabra_random == palabra[0]:
            print(palabra)

def run():
    read()


if __name__ == "__main__":
    run()