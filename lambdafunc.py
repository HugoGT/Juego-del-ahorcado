from functools import reduce
from os import mkdir

def run():
    my_list = [1, 2, 3, 4, 5, 0]

    odd = list(filter(lambda x: x%2 != 0, my_list))

    print(odd)

    squares = list(map(lambda x: x**2, my_list))
    
    print(squares)

    all_multiplied = reduce(lambda a, b: a + b, my_list)

    print(all_multiplied)


if __name__ == "__main__":
    run()