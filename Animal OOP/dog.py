from animal import Animal



class Dog(Animal):
    number_of_dogs = 0

    def __init__(self, dog_name, dog_colour):
        # calling the super class constructor
        super().__init__(dog_name, dog_colour)
        Dog.number_of_dogs += 1

    def bark(self):
        print("Woof woof")

    def __str__(self):
        return "Woof! My name is " + self._name + " and I am " + self._colour

    def set_sleep(self):
        print("I love to sleep all day ZZZZZZZZZZ")

    def get_fav_thing_chase(self, thing):
        print("I like to chase ", thing)

    def get_fav_toy(self, toy):
        print("My favorite toy is my", toy)
