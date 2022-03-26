from typing import List, Tuple
'''
C. Соседи
'''

# 181ms | 16.82Mb
def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    nbg = []
    l = len(matrix[0])  # кол-во столбцов матрицы (кол-во элементов в нулевом массиве)
    m = len(matrix)     # кол-во строк матрицы (кол-во элементов в массиве)

    # Ищем соседние элементы по горизонтали
    if l > 1: # проверяем: если матрица из одного столбца, то соседних элементов по горизонтали у нее нет
        if 0 < col < l-1:
            nbg.append(matrix[row][col-1])  # добавляем элемент слева
            nbg.append(matrix[row][col+1])  # добавляем элемент справа
        elif col == 0:
            nbg.append(matrix[row][col+1])  # добавляем элемент справа
        else:
            nbg.append(matrix[row][col-1])  # добавляем элемент слева

    # Ищем соседние элементы по вертикали
    if m > 1: # проверяем: если матрица из одного столбца, то соседних элементов по горизонтали у нее нет
        if row == 0:
            nbg.append(matrix[1][col])  # добавляем элемент снизу
        elif row == m-1:
            nbg.append(matrix[row-1][col])  # добавляем элемент сверху
        else:
            nbg.append(matrix[row-1][col])  # добавляем элемент снизу
            nbg.append(matrix[row+1][col])  # добавляем элемент сверху

    # сортируем массив по возрастанию
    nbg.sort()
    print('nbg:', nbg)
    return nbg


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())

    print('n: ', n, ', m: ', m)
    print('rows:', row, ', cols: ', col)
    print(matrix)
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
