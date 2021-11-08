def run():
    palindrom = lambda string: string == string[::-1]
    print(palindrom("ana"))

if __name__ == "__main__":
    run()