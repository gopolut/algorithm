from typing import List, Tuple
'''C. Скользящее среднее
https://contest.yandex.ru/contest/26365/problems/C/
'''

# Пусть длина входного списка с данными будет равна N, а окно сглаживания — K. В коде есть два вложенных цикла:
# внешний выполняет ровно N-K+1 итераций;
# внутренний выполняет K итераций на каждой из N-K+1 итераций внешнего цикла.
# Алгоритм выполняет примерно N×K операций


# def moving_average(arr: List[int], window_size: int) -> List[float]:
#     average = []
#     avg_num = 0
#     end = window_size
#     for idx in range(0, len(arr) - window_size + 1):
#         end = idx + window_size
#         for number in arr[idx:end]:
#             avg_num += number
#         average.append(avg_num/window_size)
#         avg_num = 0
#     return average


# МЕТОД ДВУХ УКАЗАТЕЛЕЙ
# работает быстрее примерно в K раз.
# получается порядка N - K + K = N
def moving_average(arr: List[int], window_size: int) -> List[float]:
    average = []
    # avg_num = 0
    end = window_size
    i = 0
    arr2 = arr[i:window_size]
    avg_num = sum(arr[i:window_size])
    average.append(avg_num/window_size)
    for j in range(0, len(arr) - window_size):
        avg_num = (avg_num - arr[j]) + arr[j + window_size]
        average.append(avg_num/window_size)
    return average


if __name__ == '__main__':

    def read_input() -> Tuple[List[int], int]:
        n = int(input('Длина последовательности: '))
        arr = list(map(int, input('Последовательность: ').strip().split()))
        window_size = int(input('Длина окна: '))
        return arr, window_size


    arr, window_size = read_input()
    print(" ".join(map(str, moving_average(arr, window_size))))
