" " " Shell sort " " "

import random

SIZE = 100
ARRAY = [i for i in range(SIZE)]
random.shuffle(ARRAY)
print(ARRAY)

def shell_sort(array):
    " " " Shell sort func for array < 4000 elements " " "
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'
    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()
    count = 0
    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1
    print(count)

shell_sort(ARRAY)
print(ARRAY)

