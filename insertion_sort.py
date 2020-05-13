" " " Insertion sort " " "

import random

SIZE = 10
ARRAY = [i for i in range(SIZE)]
random.shuffle(ARRAY)
print(ARRAY)

def insertion_sort(array):
    " " " Insertion sort func " " "
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam

insertion_sort(ARRAY)
print(ARRAY)
