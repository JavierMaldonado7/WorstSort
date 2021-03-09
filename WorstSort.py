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
    currentTime = time.time()
    shuffles = 0
    while(SortedVerify(array) is False):
       array =  RandomizeBB(array)

       currentTime = time.time()
       shuffles = shuffles + 1
       print(array)

    else:
       reportTime = currentTime
       print("Time taken to solve: "+(str((reportTime/777600000)))+" seconds.")
       print("Amount of shuffles done to solve: "+ str(shuffles))
       return array

array = [9,8,5,7,3]
print(WorstSort(array))