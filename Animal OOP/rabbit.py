from animal import Animal


class Rabbit(Animal):
    number_of_rabbits = []

    def __int__(self, rabbit_name, rabbit_colour):
        super().__init__(rabbit_name, rabbit_colour)
        Rabbit.number_of_rabbits += 1

    def __str__(self):
        return "My name is " + self._name + " and I am " + self._colour

    def play(self, item):
        print("I like to play with", item)

    def size(self, size):
        print("I am", size)
