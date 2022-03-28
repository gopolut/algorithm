'''
I. Степень четырёх
'''
# 46ms | 4.00Mb

def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True

    while number >= 1:
        number = number / 4
        if number == 1:
            return True
    return False

print(is_power_of_four(int(input())))
