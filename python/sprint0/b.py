from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    zip_list = []
    # for i in range(len(a)):
    #     zip_list.append(a[i])
    #     zip_list.append(b[i])
    [a[i], b[i + 1] for i in a]
    return zip_list


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
