import random
# asking for 1 random integer from range 0:50
num = random.randint(0, 50)
print(num)
# creating a list of 6 UNIQUE random numbers
# create an empty set,
# using a while loop while length of set is less than 6:
# add a random number between 1 and 50
# print 6 random numbers
lotto_num = set()
while len(lotto_num) < 6:
    lotto_num.add(random.randint(1, 50))
print(lotto_num)
