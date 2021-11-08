def run():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    new_list = filter(lambda number: number % 2 == 0, my_list)
    print(new_list)

if __name__ == "__main__":
    run()