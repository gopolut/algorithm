def wardrobe(array, length):
    if length == 0:
        return 0
    counted = [0] * (length + 1)

    for value in array:
        counted[value] += 1

    result = []
    for j in range(0, length + 1):
        result += [j] * counted[j]

    return result


if __name__ == '__main__':
    quantity = int(input())
    if quantity > 0:
        array = list(map(int, input().split(' ')))
        print(wardrobe(array, quantity))
