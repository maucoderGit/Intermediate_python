from os import WIFCONTINUED
from random import randint


def read():
    with open("./files/words.txt", "r", encoding="utf-8") as f:
        words = [line for line in f]
        lenght = int(len(words))
    return words[randint(0, lenght - 1)]

    # We rest 1 because last number will be an error


def hangman(letter, word):
    lifes = 7
    winner = False
    try:
        while lifes > 0 or winner == False:
            if len(letter) != 1:
                raise ValueError("Debes ingresar solo un caracter.")
            pass


    except ValueError:
        pass


def run():
    try:
        word = read()
        print("Bienvenido a el juego del ahorcado\n")
        user_letter = str(input("Escribe una letra: "))

    except ValueError:
        print("Solo puedes ingresar texto.")
        run()


if __name__ == "__main__":
    run()