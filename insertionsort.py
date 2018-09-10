import random

testList = []
size = 12
maxNumber = 10
minNumber = -10

for i in range(0, size):
    testList.append(random.randint(minNumber, maxNumber))

def insertionsort(liste):

    n = len(liste)

    for i in range(1, n):
        valuetosort = liste[i]
        k = i

        while k > 0 and valuetosort < liste[k - 1]:
            liste[k] = liste[k - 1]
            k -=1
        liste[k] = valuetosort

    return liste

print(testList)
print(insertionsort(testList))