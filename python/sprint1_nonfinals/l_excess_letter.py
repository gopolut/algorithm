from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    a = list(shorter)
    b = list(longer)

    sum_a = sum(list(map(ord, a)))
    sum_b = sum(list(map(ord, b)))

    dif = abs(sum_a - sum_b)
    left = chr(dif)
    print(sum_a, sum_b)
    return left


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
