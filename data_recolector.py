# First Intermediate Python Proyect

from platzi_workers import DATA

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker["age"] >= 18 , DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    # for worker in all_python_devs:
    #     print(worker)

    # for worker in all_Platzi_workers:
    #     print(worker)

    for worker in adults:
        print(worker)


if __name__ == "__main__":
    run()