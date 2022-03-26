from typing import List, Tuple
'''
C. Соседи
'''

# 189ms | 15.59Mb 

def get_neighbours(matrix, coor_row, coor_col, row_count, col_count):
    numbers = []
    # слева/справа
    if coor_row > 0:
        numbers.append(matrix[coor_row - 1][coor_col])
    if coor_row < row_count - 1:
        numbers.append(matrix[coor_row + 1][coor_col])

    # снизу/сверху
    if coor_col > 0:
        numbers.append(matrix[coor_row][coor_col - 1])
    if coor_col < col_count - 1:
        numbers.append(matrix[coor_row][coor_col + 1])
    
    numbers.sort()
    return numbers


def transform(list):
    list_of_nums = [int(number) for number in list]
    return list_of_nums


if __name__ == '__main__':

    row_count = int(input()) # кол-во строк
    col_count = int(input()) # кол-во рядов

    matrix = [transform(input().split()) for _ in range(row_count)]

    coor_row = int(input())
    coor_col = int(input())

    # print(' '.join(map(str, get_neighbours(matrix, coor_row, coor_col, row_count, col_count))))
    print(*get_neighbours(matrix, coor_row, coor_col, row_count, col_count))

