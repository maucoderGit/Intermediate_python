def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("You can't use empity strings")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        word = input("Ingresa una frase o palabra: ")
        print(palindrome(word))
    except TypeError:
        print("Not avalible data type, You can only use strings!")


if __name__ == "__main__":
    run()