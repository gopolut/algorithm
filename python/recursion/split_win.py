# Сложение чисел в массиве припомощит рекурсии и алгоритма разделяй и вляствуй
# p.s. Пример из книги "Грокаем алгоритмы"


def sum_win(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_win(array[1:])


print(sum_win([1, 4, 5, 9]))
