" " " Selection sort " " "

import random

SIZE = 10
ARRAY = [i for i in range(SIZE)]
random.shuffle(ARRAY)
print(ARRAY)

def selection_sort(array):
    " " " Selection sort func " " "
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j

        array[idx_min], array[i] = array[i], array[idx_min]


selection_sort(ARRAY)
print(ARRAY)
