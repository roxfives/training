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
    selectionSort(vector)
    print('sorted: ' + str(vector))

# Function to swap elements in the positions i and j of the vector vet
def swap(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux

# A simple selectionSort function
def selectionSort(vet):
    if(len(vet) <= 1): # Checks if it's necessary to order the vector
        return

    i = 0
    length = len(vet)
    while(i < length):
        mim = i
        j = i
        while(j < length):
            if(vet[j] < vet[mim]):
                mim = j
            
            j += 1
            
        swap(vet, i, mim)
        i += 1

# Calls main
if __name__ == '__main__':
    main()