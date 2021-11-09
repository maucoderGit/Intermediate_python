# First Intermediate Python Proyect

from platzi_workers import DATA

def run():
    # Class Examples

    # all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    # all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    # adults = list(filter(lambda worker: worker["age"] >= 18 , DATA))
    # adults = list(map(lambda worker: worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] > 70}, DATA))

    # Challenge

    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    all_python_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_python_workers = list(map(lambda worker: worker["name"], all_python_workers))

    adults = [worker["name"] for worker in DATA if worker["age"] >= 18]
    old_people = [worker["age"] for worker in DATA if worker["age"] > 70] 

    for worker in adults:
        print(worker)

    # Class Executions:
    
    # for worker in all_python_devs:
    #     print(worker)

    # for worker in all_Platzi_workers:
    #     print(worker)

    for worker in old_people:
        print(worker)


if __name__ == "__main__":
    run()