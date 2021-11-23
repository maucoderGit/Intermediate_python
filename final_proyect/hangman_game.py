from random import randint


def get_word() -> str:
    with open("../final_proyect/files/words.txt", "r", encoding="utf-8") as f:
        words = [line.replace("\n", "") for line in f]
        lenght = int(len(words))
    return words[randint(0, lenght - 1)]

    # We rest 1 because last number will be an error


def secret_word(word: str) -> str:
    for i in word:
        word = word.replace(i, "_ ")
    return word


def validator(word: str, letter: str) -> list:
    index_array = []
    count = 0

    for i in word:
        if i == letter:
            index_array.append(count)
            print(index_array)
        count += 1
    
    return index_array


def replacer(word, user_letter, secret_word) -> str:
    accerts = validator(word, user_letter)
    
    if len(accerts) == 0:
        return False
    
    for i in accerts:
        secret_word[i] = user_letter

    return secret_word


def run():
    word = get_word()
    print(word)
    ocult_word = secret_word(word)
    print(ocult_word)

    try:
        print("Bienvenido a el juego del ahorcado\n")
        user_letter = input("Escribe una letra: ")
        ocult_word = replacer(word, user_letter, ocult_word)
        print(ocult_word)

    except ValueError:
        print("Solo puedes ingresar texto.")
        run()


if __name__ == "__main__":
    run()