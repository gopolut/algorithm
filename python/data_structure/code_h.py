from typing import List

# H. Скобочная последовательность
# -------------------------------
# Дана скобочная последовательность. Нужно определить, правильная ли она

# 61ms | 4.03Mb


def result(lst_brakets: List[str]) -> bool:
    close = (']', ')', '}')
    open = ('[', '(', '{')

    pairs = []

    if len(lst_brakets) == 0:
        return True

    if lst_brakets[0] in close:
        return False

    if lst_brakets[-1] in open:
        return False

    if len(lst_brakets) % 2 != 0:
        return False

    for i in lst_brakets:
        if i in open:
            pairs.append(i)
        else:
            if len(pairs) == 0:
                return False
            if abs(ord(i) - ord(pairs[-1])) > 2:
                return False
            pairs.pop()
    return True


def read_input() -> List[str]:
    brakets = str(input())
    brakets_list = list(brakets)
    return brakets_list


def main():
    str_br = read_input()
    print(result(str_br))


if __name__ == '__main__':
    main()
