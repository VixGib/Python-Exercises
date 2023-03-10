from animal import Animal




class Cat(Animal):

    number_of_cats = 0

    def __init__(self, cat_name, cat_colour):
        super().__init__(cat_name, cat_colour)
        Cat.number_of_cats += 1

    def __str__(self):
        return "Meeeooowwww! My name is " + self._name + " and I am " + self._colour

    def purr(self):
        print("Purr purr")

    def hunt(self, thing):
        print("Yum yum, I like hunting for ", thing)

    def make_sound(self):
        return "Meow meow"

    def set_height(self, cat_height):
        self._height = cat_height

    def set_name(self, newName):
        self._name = newName