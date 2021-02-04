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
        sortValue = liste[i]
        k = i

        while k > 0 and sortValue < liste[k - 1]:
            liste[k] = liste[k - 1]
            k -=1
        liste[k] = sortValue
    return liste


print("Unsorted list:\n" + str(testList) + "\n")
print("Insertion sorted list:\n" + str(insertionsort(testList)))