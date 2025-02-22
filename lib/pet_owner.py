class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of Pet.")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
