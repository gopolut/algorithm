from typing import Tuple, List

'''
B. Ловкость рук
ID: 64998102
'''


def sleight_of_hand(trainer: List[List[str]], keys_count: int) -> int:
    list_of_int = []
    points = 0
    for i in range(0, len(trainer)):
        for j in trainer[i]:
            if j != '.':
                list_of_int.append(int(j))

    # Если переданы только точки
    if len(list_of_int) == 0:
        return 0

    set_list = set(list_of_int)
    for x in set_list:
        int_count = list_of_int.count(x)
        if int_count <= keys_count * 2:
            points += 1
    return points


def read_input() -> Tuple[List[List[str]], int]:
    keys_count = int(input())
    trainer = []
    for i in range(4):
        trainer.append(list(str(input())))

    return keys_count, trainer


def main():
    keys_count, trainer = read_input()
    print(sleight_of_hand(trainer, keys_count))


if __name__ == '__main__':
    main()

