#!/usr/bin/python0

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
for i in Belgium:
    print("-")

Belgium2 = Belgium.replace(",", ":")
print(Belgium2)

Belgium3 = Belgium.split(",")
print(Belgium3)

print(int(Belgium3[1]) + int(Belgium3[3]))
