from data_structures.queue import Queue

class Dog:
    def __init__(self, name=None):
        self.species = "dog"
        self.name = name if name is not None else "no name"

class Cat:
    def __init__(self, name=None):
        self.species = "cat"
        self.name = name if name is not None else "no name"

class AnimalShelter:
    def __init__(self):
        self.animals = Queue()

    def enqueue(self, animal):
        if not isinstance(animal, (Dog, Cat)):
            raise ValueError("must be a Dog or Cat")
        self.animals.enqueue(animal)

    def dequeue(self, pref):
        if pref not in ["dog", "cat"]:
            return None

        adopted = None
        temp = []

        while not self.animals.is_empty():
            animal = self.animals.dequeue()
            if adopted is None and animal.species == pref:
                adopted = animal
            else:
                temp.append(animal)

        for animal in temp:
            self.animals.enqueue(animal)

        return adopted
