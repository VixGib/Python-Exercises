
from cat import Cat

catObj = Cat("Agnes", "grey")
animals = []
animals.append(catObj)
print(catObj)
catObj.purr()
catObj.hunt("mice")
catObj.fav_human("Martina's Kids")
print(catObj.make_sound())
catObj.legs(4)
catObj.gender("Girl")
catObj.fav_food("Tuna")
catObj.age(4)


catObj2 = Cat("Bentley", "Black and White")
animals.append(catObj2)
print(catObj2)
catObj2.purr()
catObj2.hunt("Birds")
catObj2.fav_human("Alex")
print(catObj2.make_sound())
catObj2.legs(4)
catObj2.gender("Boy")
catObj2.fav_food("Salmon")
catObj.age(7)
