from typing import Tuple, List

'''
A. Ближайший ноль
ID: 64997580
'''


def nearest_null(number_list: List[int], street_length: int) -> List[int]:
    counter = 0
    distance = []
    for idx in range(0, len(number_list)):
        if number_list[idx] == 0 and idx > 0:
            counter = 1
            # если нуля нет в массиве,
            # т.е. 1-й элемент списка не равен нулю
            if 0 not in distance:
                while idx - counter >= 0:
                    distance[idx - counter] = counter
                    counter += 1
            else:
                while distance[-counter] - 1 >= counter:
                    distance[idx - counter] = counter
                    counter += 1
            counter = 0
        elif number_list[idx] == 0:
            counter = 0
        else:
            counter += 1
        distance.append(counter)

    return distance


def read_input() -> Tuple[int, List[int]]:
    street_length = int(input())
    # number_list = list(map(int, input().strip().split()))
    number_list = [int(sign) for sign in input().split()]
    return street_length, number_list


def main():
    street_length, number_list = read_input()
    print(*nearest_null(number_list, street_length))


if __name__ == '__main__':
    main()
