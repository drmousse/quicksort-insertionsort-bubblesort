import random

testList = []
size = 20
maxNumber = 100
minNumber= -100

for i in range(0, size):
    testList.append(random.randint(minNumber, maxNumber))

def quicksort(liste):

    if len(liste) <= 1:
        return liste

    pivot = len(liste) - 1
    left = 0
    right = len(liste) - 2

    cond = True

    while cond:
        while left <= right and liste[left] <= liste[pivot]:
            left += 1
        while right >= left and liste[right] >= liste[pivot]:
            right -= 1
        if right < left:
            cond = False
        else:
            temp = liste[left]
            liste[left] = liste[right]
            liste[right] = temp

    temp = liste[left]
    liste[left] = liste[pivot]
    liste[pivot] = temp

    return quicksort(liste[:left]) + quicksort(liste[left:])

print("Unordered list: \n" + str(testList) + "\n")
print("List after Quick Sort Algorithm: \n" + str(quicksort(testList)))