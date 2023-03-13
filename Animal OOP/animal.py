# super class
class Animal:

    # superclass constructor
    def __init__(self, an_name, an_colour):
        self._name = an_name
        self._colour = an_colour

    def get_make_sound(self):
        return " "

    def set_sleep(self):
        print("ZZZZZZZZZZZZ")

    def set_gender(self, gender):
        print("I am a ", gender)

    def set_legs(self, number):
        print("I have ", number, "legs")

    def set_fav_human(self, name):
        print("My favourite human is", name)

    def get_fav_food(self, food):
        print("My favourite food is",food)

    def set_age(self, age):
        print("I am", age, "years old")
