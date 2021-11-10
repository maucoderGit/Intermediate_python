def divisors(num):
    try: 
        if num < 0:
            raise ValueError("Ingresa un número positivo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors

    except ValueError as ve:
        print(ve)


def run():
    try:
        num = int(input("ingresa un número: "))
        print(divisors(num) or "No pude ejecutar esto.")
        print("Termino el programa")
    
    except ValueError:
        print("debes ingresar un número")


if __name__ == "__main__":
    run()