# A. Поиск в сломанном массиве
# ID: 66115374
from typing import List


def broken_search(numbers: List[int], target: int) -> int:
    left: int = 0
    right: int = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        if numbers[left] <= numbers[middle]:
            if numbers[left] <= target < numbers[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if numbers[middle] < target <= numbers[right]:
                left = middle + 1
            else:
                right = middle - 1
    return -1


if __name__ == '__main__':
    _ = int(input())
    target: int = int(input())

    numbers: List[int] = [int(num) for num in input().split(' ')]
    # numbers = list(map(int, input().split(' ')))
    print(broken_search(numbers, target))
