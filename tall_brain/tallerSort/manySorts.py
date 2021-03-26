"""
    Harper Scott
    March __th, 2021
    Colin Reilly's School of Brogramming
"""

import random

def insertionSort(rawList):
    """
    Insertion sort function.

    Keyword Arguments:
    rawList -- List of integers to be sorted.
    """

    print(rawList)

    for n in range(1, len(rawList)):
        
        key = rawList[n]
        prev = rawList[n-1]
        while key < prev:
            if key < prev == True:
                
            prev, key = key, prev
            if key > prev:
                pass

    return rawList

def selectionSort(rawList):
    """
    Selection sort function.

    Keyword Arguments:
    rawList -- List of integers to be sorted.
    """
    pass


dickTime = [random.randint(0, 10) for n in range(10)]
print(insertionSort(dickTime))
