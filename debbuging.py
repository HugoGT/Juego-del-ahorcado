def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise ValueError("No se pueden ingresar números negativos")
        print(divisors(num))
        print("Termino del programa")
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    run()