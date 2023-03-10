# super class
class Animal:

    # superclass constructor
    def __init__(self, an_name, an_colour):
        self._name = an_name
        self._colour = an_colour

    def make_sound(self):
        return " "

    def sleep(self):
        print("ZZZZZZZZZZZZ")

    def gender(self, gender):
        print("I am a ", gender)

    def legs(self, number):
        print("I have ", number, "legs")

    def fav_human(self, name):
        print("My favourite human is", name)

    def fav_food(self, food):
        print("My favourite food is",food)

    def age(self, age):
        print("I am", age, "years old")
