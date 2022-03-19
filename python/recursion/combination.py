# B. Комбинации


buttons = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


# подходит для 2-х цифр
# def comd(first, second):
#     output = ''
#     comb = ''
#     for i in buttons[first]:
#         for j in buttons[second]:
#             print(i + j)
#             comb = i + j
#             output += comb + ' '
#     print(output)


def combinations(input_string):
    if input_string == '':
        return ['']

    data = []
    word = buttons[input_string[-1]]

    for combination in combinations(input_string[:-1:]):
        for c in word:
            data.append(combination + c)

    return data


if __name__ == '__main__':
    print(' '.join(combinations(input())))
