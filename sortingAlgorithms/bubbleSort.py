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
    bubbleSort(vector)
    print('sorted: ' + str(vector))

# Function to swap elements in the positions i and j of the vector vet
def swap(vet, i, j):
    aux = vet[i]
    vet[i] = vet[j]
    vet[j] = aux

# A simple bubbleSort function to warm up :)
def bubbleSort(vet):
    if(len(vet) <= 1): # Checks if it's necessary to order the vector
        return

    swaped = True
    length = len(vet) 
    while swaped:
        swaped = False
        for i in range(0, length-1): 
            if(vet[i] > vet[i+1]):
                swap(vet, i, i+1)
                swaped = True

# Calls main
main()