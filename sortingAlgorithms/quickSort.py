#! /usr/bin/python2
import random as rand

# The entry point
def main():
    vector = range(0, 10)

    i = 0
    while(i < len(vector)):
        vector[i] = rand.randint(0, 10)
        i += 1

    print('unsorted: ' + str(vector))
    quickSort(vector, 0, len(vector))
    print('sorted: ' + str(vector))

# Function to swap elements in the positions i and j of the vector vet
def swap(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux

def quickSort(vec, begin, end):
    if(end - begin <= 0):
        return

    pivot = begin
    storeIndex = begin + 1
    for i in range(begin+1, end):
        if(vec[i] < vec[pivot]):
            swap(vec, i, storeIndex)
            storeIndex += 1
        
    swap(vec, pivot, storeIndex-1)
    quickSort(vec, begin, storeIndex-1)
    quickSort(vec, storeIndex, end)

if __name__ == '__main__':
    main()