DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]   


def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    for worker in all_python_devs:
        print(worker)

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "platzi"]

    for worker in all_platzi_workers:
        print(worker)

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))

    for worker in adults:
        print(worker)

    old = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
    old = list(map(lambda worker: worker ["old"], old))

    for worker in old:
        print(worker)

    python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    python_devs = list(map(lambda worker: worker["name"], python_devs))

    for worker in python_devs:
        print(worker)

    platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    platzi_workers = list(map(lambda worker: worker["name"], platzi_workers))

    for worker in platzi_workers:
        print(worker)

    adults_2 = [worker["name"] for worker in DATA if worker["age"] > 20]

    for worker in adults_2:
        print(worker)

    old_2 = [worker | {"old": worker["age"] > 70} for worker in DATA]
    old_2 = [worker["name"] for worker in old_2 if worker["old"] == True]

    for worker in old_2:
        print(worker)


if __name__ == "__main__":
    run()