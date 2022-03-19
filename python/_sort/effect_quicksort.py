# B. Эффективная быстрая сортировка
# ID: 66115446
import collections
import random
from typing import Any, List, Tuple


def partition(users: List[Tuple[int, int, str]], low: int, high: int) -> Tuple[int, int]:
    left: int = low
    right: int = high
    pivot: int = users[random.randint(low, high)]

    while left <= right:
        while users[left] < pivot:
            left += 1
        while users[right] > pivot:
            right -= 1
        if left <= right:
            users[left], users[right] = users[right], users[left]
            left += 1
            right -= 1
    return left, right


def quick_sort(users: List[Tuple[int, int, str]], low: int, high: int) -> Any:
    if low >= high:
        return -1
    left, right = partition(users, low, high)
    quick_sort(users, low=low, high=right)
    quick_sort(users, low=left, high=high)


User = collections.namedtuple('User', ['task', 'penalty', 'name'])


def transform(name: str, task: str, penalty: str) -> User:
    # user[1] = -int(user[1])
    # user[2] = int(user[2])
    # user = User(user[1], user[2], user[0])
    task = -int(task)
    penalty = int(penalty)
    return User(task, penalty, name)
    # return user


if __name__ == '__main__':
    number: int = int(input())
    users: List[User] = [
        transform(*input().split()) for _ in range(number)
        ]

    quick_sort(users, low=0, high=number-1)
    print('\n'.join([user.name for user in users]))
