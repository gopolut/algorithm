from typing import List, Tuple, Optional

'''D. Две фишки'''

# Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
# Если таких пар несколько, то можно вывести любую из них.

# Примерно N^2/2 в худшем случае
# Примерно N^2/4 в среднем


# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     for first in range(0, len(arr)):
#         for second in range(first+1, len(arr)):
#             if arr[first] + arr[second] == target_sum:
#                 return arr[first], arr[second]
#     return None


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set()
    for number in arr:
        element = target_sum - number
        if element in previous:
            return number, element
        else:
            previous.add(number)
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
