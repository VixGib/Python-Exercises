
from cat import Cat

catObj = Cat("Agnes", "grey")
animals = []
animals.append(catObj)
print(catObj)
catObj.set_purr()
catObj.set_hunt("mice")
catObj.set_fav_human("Martina's Kids")
print(catObj.get_make_sound())
catObj.set_legs(4)
catObj.set_gender("Girl")
catObj.get_fav_food("Tuna")
catObj.set_age(4)


catObj2 = Cat("Bentley", "Black and White")
animals.append(catObj2)
print(catObj2)
catObj2.set_purr()
catObj2.set_hunt("Birds")
catObj2.set_fav_human("Alex")
print(catObj2.get_make_sound())
catObj2.set_legs(4)
catObj2.set_gender("Boy")
catObj2.get_fav_food("Salmon")
catObj.set_age(7)
