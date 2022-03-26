from typing import List, Tuple, Optional

'''E. Две фишки - 2'''
# Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
# Если таких пар несколько, то можно вывести любую из них.


# наивный алгоритм
# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 return arr[i], arr[j]
#     return None


# АЛГОРИТМ со структурой данных поиска
def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    secondary = set()
    for number in arr:
        element = target_sum - number
        if element in secondary:
            return element, number
        else:
            secondary.add(number)
    return None


if __name__ == '__main__':
    
    def read_input() -> Tuple[List[int], int]:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        target_sum = int(input())
        return arr, target_sum


    def print_result(result: Optional[Tuple[int, int]]) -> None:
        if result is None:
            print(None)
        else:
            print(" ".join(map(str, result)))


    arr, target_sum = read_input()
    print_result(two_sum(arr, target_sum))
