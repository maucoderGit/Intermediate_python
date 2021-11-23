from random import randint
import os

def user_input() -> str:
    letter: str= input("Escribe una letra: ")
    while len(letter) != 1:
        print("Debes ingresar una letra")
        letter: str= input("Escribe una letra: ")

    return letter


def get_word() -> str:
    with open("./final_proyect/files/words.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n", "") for line in f]
        lenght = int(len(words))
    return words[randint(0, lenght)]

    # We rest 1 because last number will be an error


def secret_word(word: str) -> str:
    for i in word:
        word = word.replace(i, "_")
    return word


def validator(word: str, letter: str) -> list:
    index_array = []
    count = 0

    for i in word:
        if i == letter:
            index_array.append(count)
        count += 1

    return index_array


def replacer(word: str, user_letter: str, secret_word: str) -> str:
    accerts: list = validator(word, user_letter)
    array_word: list = list(secret_word)
    os.system("clear")

    if len(accerts) == 0:
        print("La letra es incorrecta!")
        return secret_word

    for i in accerts:
        array_word[i] = user_letter

    secret_word = "".join(array_word)
    return secret_word


def game(word: str) -> bool:
    my_word: tuple = tuple(map(lambda i: i == "_", word))

    for i in my_word:
        if i == True:
            return False
    
    return True


def run():
    print("Bienvenido a el juego del ahorcado\n")

    word = get_word()
    ocult_word = secret_word(word)

    try:
        while game(ocult_word) == False:
            print(ocult_word + "\n")
            user_letter = user_input()
            ocult_word = replacer(word, user_letter, ocult_word)

        print(ocult_word + " \nGanaste!")

    except TypeError:
        print("Solo puedes ingresar texto.")


if __name__ == "__main__":
    run()