import unittest
from lib.pet_owner import Owner, Pet

class TestPetOwner(unittest.TestCase):
    def setUp(self):
        self.owner = Owner("Miriam")
        self.pet1 = Pet("Buddy", "dog")
        self.pet2 = Pet("Mittens", "cat")

    def test_add_pet(self):
        self.owner.add_pet(self.pet1)
        self.assertIn(self.pet1, self.owner.pets)

    def test_get_sorted_pets(self):
        self.owner.add_pet(self.pet1)
        self.owner.add_pet(self.pet2)
        sorted_pets = self.owner.get_sorted_pets()
        self.assertEqual(sorted_pets, [self.pet1, self.pet2])  # Buddy should come before Mittens

    def test_invalid_pet_type(self):
        with self.assertRaises(Exception):
            Pet("Goldie", "fish")  # Invalid pet type

    def test_add_invalid_pet(self):
        with self.assertRaises(Exception):
            self.owner.add_pet("NotAPet")  # Invalid pet instance

if __name__ == "__main__":
    unittest.main()
