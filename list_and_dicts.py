def run():
    super_list = [
        {"firstname": "Mauricio", "lastname": "González"},
        {"firstname": "Juan", "lastname": "Puertas"},
        {"firstname": "Lucia", "lastname": "Torres"},
        {"firstname": "Maria","lastname": "Cruz"}
    ]

    super_dict = {
        "integer_nums": [1, 2, 3, 4, 5],
        "natural_nums": [-1, -2, 0, 3, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4]
    }

    for value in super_list:
        for key, value in value.items():
            print(key, "-", value)

    for key, value in super_dict.items():
        print(key, "-", value)


if __name__ == "__main__":
    run()