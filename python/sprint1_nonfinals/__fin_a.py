
def nearest_null(numbers, length):
    counter = 0
    nearest = []
    for idx in range(0, len(numbers)):
        # итерация доходит до нуля, если ноль не первый в списке
        if idx > 0 and numbers[idx] == 0:
            counter = 1
        # если ноль есть в массиве nearest
            if 0 in nearest:
                # while nearest[-counter] - 1 >= counter:
                #     nearest[idx - counter] = counter
                #     counter += 1
                while nearest[-counter] >= counter:
                    nearest[-counter] = counter
                    counter += 1
                # for i in range(len(nearest)-1, -1, -1):
                #     if nearest[i] != counter:
                #         i = counter
                #     counter += 1
        # если нуля нет в массиве nearest
            else:
                # while idx - counter >= 0:
                #     nearest[idx - counter] = counter
                #     counter += 1
                # for i in reversed(nearest):
                for i in range(len(nearest)-1, -1, -1):
                    nearest[i] = counter
                    counter += 1

            counter = 0
        elif numbers[idx] == 0:
            counter += 0
        else:
            counter += 1
        nearest.append(counter)
    return nearest


if __name__ == '__main__':
    length = int(input())
    numbers = [int(sign) for sign in input().split()]

    print(*nearest_null(numbers, length))
