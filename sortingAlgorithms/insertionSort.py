#!/usr/bin/python2
import random as rand

# The entry point
def main():
    vector = range(0, 10)

    i = 0
    while(i < len(vector)):
        vector[i] = rand.randint(0, 100)
        i += 1

    print('unsorted: ' + str(vector))
    insertionSort(vector)
    print('sorted: ' + str(vector))

# A simple insertion sort
def insertionSort(vet):
    if(len(vet) <= 1): # Checks if it's necessary to order the vector
        return

    sorting = 1
    length = len(vet)
    while(sorting < length):
        newPos = sorting
        while(newPos >= 0 and vet[newPos] >= vet[sorting]):
            newPos -= 1

        vet.insert(newPos + 1, vet.pop(sorting))
        sorting += 1

# Calls main
if __name__ == '__main__':
    main()