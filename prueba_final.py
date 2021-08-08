import random



def read():
    data = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append((line))
    data = enumerate(data)
    print(data)

def run():
    read()


if __name__ == "__main__":
    run()