#WorstSort
#Javier Maldonado Rivera
#3/4/2021
import random
import time

def SortedVerify(array):
    l = 1
    for n in array:
        if(l == len(array)):
            return True
        if(n > array[l]):
            return False

        l = l + 1

def RandomizeBB(array):
    random.shuffle(array)
    return array


def WorstSort(array):
    initTime = time.time()
    currentTime = time.time()
    while(SortedVerify(array) is False):
       array =  RandomizeBB(array)
       reportTime = currentTime - initTime
       currentTime = time.time()

    else:
       print(reportTime)
       return array

array = [9,8,5,8]
print(WorstSort(array))