from random import randint


def get_word() -> str:
    with open("../final_proyect/files/words.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n", "") for line in f]
        lenght = int(len(words))
    return words[randint(0, lenght - 1)]

    # We rest 1 because last number will be an error


def secret_word(word: str) -> str:
    for i in word:
        print(i)
        word = word.replace(i, "_ ")
    return word


def validator(word: str, letter: str):
    # secret_word = open
    print(secret_word)
    return secret_word


def run():
    word = get_word()
    ocult_word = secret_word(word)
    print(ocult_word)

    try:
        print("Bienvenido a el juego del ahorcado\n")
        user_letter = input("Escribe una letra: ")
        ocult_word = validator(word, user_letter)

    except ValueError:
        print("Solo puedes ingresar texto.")
        run()


if __name__ == "__main__":
    run()