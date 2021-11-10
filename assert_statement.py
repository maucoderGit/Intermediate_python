def divisors(num):
        if num < 0:
            raise ValueError("Ingresa un número positivo")
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    num = input("ingresa un número: ")
    
    assert num.isnumeric(), "debes ingresar un número"
    
    print(divisors(int(num)))
    print("Termino el programa")
    


if __name__ == "__main__":
    run()