#WorstSort
#Javier Maldonado Rivera
#3/4/2021
import random
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
    while(SortedVerify(array) is False):
       array =  RandomizeBB(array)
       print(array)
    else:
       return array

array = [9,6,3]
print(WorstSort(array))