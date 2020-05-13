" " "   Закодируйте любую строку по алгоритму Хаффмана.    " " "

import operator
from collections import OrderedDict

string = "beep boop beer!"
print(f'Входная строка: {string}')

# создадим класс нода
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

# посчитаем количество вхождений символа в строку
symb = {}

for ch in string:
    if ch not in symb:
        symb.update({ch : 1})
    else:
        n = symb.get(ch) + 1
        symb.update({ch : n})

# посчитем длинну строки
LEN = len(symb)

# сортировка по количеству вхождений
symb = OrderedDict(sorted(symb.items(), key=operator.itemgetter(1), reverse=True))
print(f"\nЧастота вхождений символов в строку:\n{symb}")

# построим дерево
for i in range(LEN - 1):
    ch_1, w_1 = symb.popitem()
    ch_2, w_2 = symb.popitem()
    node = Node(left=ch_1, right=ch_2)
    symb.update({node : w_1 + w_2})
    symb = OrderedDict(sorted(symb.items(), key=operator.itemgetter(1), reverse=True))

# функция, присваивающая индексы буквам, по положению в дереве
codes = {}
def alg2(elem, counter):
        if type(elem.left) == Node and type(elem.right) == Node:
            return alg2(elem.left, counter + '0'), alg2(elem.right, counter + '1')
        elif type(elem.left) == Node and type(elem.right) != Node:
            codes.update({elem.right : counter + '1'})
            return alg2(elem.left, counter + '0')
        elif type(elem.left) != Node and type(elem.right) == Node:
            codes.update({elem.left: counter + '0'})
            return alg2(elem.right, counter + '1')
        elif type(elem.left) != Node and type(elem.right) != Node:
             codes.update({elem.left: counter + '0'})
             codes.update({elem.right : counter + '1'})

# создание словаря индексов
alg2(list(symb.keys())[0], '')

# кодируем строку
new_string = string[:]
print('\nТаблица Хаффмана')

for ch, code in codes.items():
    print(ch, code)
    for i in range(len(string)):
        if string[i] == ch:
            new_string = new_string.replace(ch, (code + "_"), 1)

print(f"\nЗакодированная строка:\n{new_string}")
