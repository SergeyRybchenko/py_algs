" " " Quicksort " " "

import random

SIZE = 10
ARRAY = [i for i in range(SIZE)]
random.shuffle(ARRAY)
print(ARRAY)

def quick_sort(array):
    " " " Quicksort recursion func " " "
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    s_ar, m_ar, l_ar = [], [], []

    for item in array:
        if item < pivot:
            s_ar.append(item)
        elif item > pivot:
            l_ar.append(item)
        elif item == pivot:
            m_ar.append(item)
        else:
            raise Exception('Случилось непредвиденное')


    print(s_ar, m_ar, l_ar)
    return quick_sort(s_ar) + m_ar + quick_sort(l_ar)

def quick_sort_no_memory(array, fst, lst):
    " " " Quicksort recursion func without using additional memory " " "
    if fst >= lst:
        return

    print(array)

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1
    
    quick_sort_no_memory(array, fst, j)
    quick_sort_no_memory(array, i, lst)


print(quick_sort(ARRAY))
print('*' * 50)
quick_sort_no_memory(ARRAY, 0, len(ARRAY) - 1)
print(ARRAY)
