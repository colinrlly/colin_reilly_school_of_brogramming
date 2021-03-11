def normal_sort(numList):
    print(numList)
    sortedList = sorted(numList)
    print(sortedList)


# normal_sort([5, 2, 4, 1, 3])


def bubble_sort(numList):
    print(numList)
    for n in range(len(numList)):
        for m in range(len(numList)-1):
            if numList[m] > numList[m+1]:
                numList[m], numList[m+1] = numList[m+1], numList[m]
        


    print(numList)


bubble_sort([42, 20, 78, 9, 15, 34, 105])
