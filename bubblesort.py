import random

testList = []
size = 20
maxNumber = 100
minNumber = -100

for i in range(0, size):
    testList.append(random.randint(minNumber, maxNumber))


def bubblesort(liste):
    n = len(liste) - 1

    while n > 0:
        for i in range(0, n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
        n -= 1

    return liste


print("Unsorted list:\n" + str(testList) + "\n")
print("Bubble sorted list:\n" + str(bubblesort(testList)))