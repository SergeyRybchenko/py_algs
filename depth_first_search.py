" " "        Программа, которая обходит не взвешенный ориентированный граф без петель," \
"        в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search)." \
"                                                                                          " \
"        Примечания:                                                                       " \
"                   a. граф должен храниться в виде списка смежности;                      " \
"                   b. генерация графа выполняется в отдельной функции,                    " \
"                      которая принимает на вход число вершин.                           " " "

def graph(N):
    graph = []
    for i in range(N):
        spam = []
        for j in range(N):
            if j != i:
                spam.append(j)
        graph.append(spam)
    return graph

def dfs_func(vertex):
    is_visited[vertex] = True
    for i in graph[vertex]:
        if not is_visited[i]:
            dfs_func(i)



N = int(input('Введите количество вершин: '))
graph = graph(N)
print(f'Граф в виде списка смежности:\n{graph}\n')
is_visited = [False] * N
dfs_func(0)
print(f'Проверяем условие, в котором все вершины связаны:\nКоличество вершин: {N}\nОбошли вершин: {is_visited.count(True)}')