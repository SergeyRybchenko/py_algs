" " " Bubble sort " " "

import random

SIZE = 10
ARRAY = [i for i in range(SIZE)]
random.shuffle(ARRAY)
print(ARRAY)

N = 1
while N < len(ARRAY):
    for i in range(len(ARRAY) - N):
        if ARRAY[i] > ARRAY[i + 1]:
            ARRAY[i], ARRAY[i + 1] = ARRAY[i + 1], ARRAY[i]
    N += 1

print(ARRAY)
