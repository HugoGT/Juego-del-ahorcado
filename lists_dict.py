def run ():
    # my_list = [1,"Hello", True, 4.5]
    # mi_dict = {"firstname": "Facundo", "lastname": "García"}

    # super_list = [
    #     {"firstname": "Facundo", "lastname": "García"},
    #     {"firstname": "Miguel", "lastname": "Torres"},
    #     {"firstname": "Pepe", "lastname": "Rodelo"},
    #     {"firstname": "Susana", "lastname": "Martinez"},
    #     {"firstname": "José", "lastname": "García"},
    # ]

    # super_dict = {
    #     "natural_nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    #     "integer_nums": [-1, -2, 0, 1, 2],
    #     "floating_nums": [1.1, 4.5, 6.45]
    # }
    
    # for key, value in super_dict.items():
    #     print(key, "-", value)
    
    # for i in super_list:
    #     print((i.items())-"dict_items")

    def run():
        squares = []
        for i in range(1,101):
            squares.append(i**2)

        print(squares)


if __name__ == "__main__":
    run()