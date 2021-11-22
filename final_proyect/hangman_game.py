from random import randint


def read():
    with open("../final_proyect/files/words.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n", "") for line in f]
        lenght = int(len(words))
    return words[randint(0, lenght - 1)]

    # We rest 1 because last number will be an error


def run():
    word = read()
    
    try:
        print(word)
        print("Bienvenido a el juego del ahorcado\n")
        user_letter = str(input("Escribe una letra: "))

    except ValueError:
        print("Solo puedes ingresar texto.")
        run()


if __name__ == "__main__":
    run()