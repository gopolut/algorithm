from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    average = []
    avg_num = 0
    end = window_size
    for idx in range(0, len(arr) - window_size + 1):
        end = idx + window_size
        for number in arr[idx:end]:
            avg_num += number
        average.append(avg_num/window_size)
        avg_num = 0
    return average


def read_input() -> Tuple[List[int], int]:
    n = int(input('Длина последовательности: '))
    arr = list(map(int, input('Последовательность: ').strip().split()))
    window_size = int(input('Длина окна: '))
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
