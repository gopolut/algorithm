# L. Два велосипеда
# Нужна рекурсия


def binary_search(list, price, left, right):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + right)//2
        # guess = list[mid]
        if list[mid] >= price and (list[mid - 1] < price or mid == 0):
            # return mid
            return mid + 1
        elif price <= money[mid]:
            right = mid
        else:
            mid += 1
    return -1


def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)


if __name__ == '__main__':
    # money = [int(num) for num in input().split(' ')]

    days = int(input())
    money = list(map(int, input().strip().split()))
    price = int(input())
    print(binary_search(money, price, left=0, right=len(money)), binary_search(money, price * 2, left=0, right=len(money)))

    # print(binarySearch(money, price, left=0, right=len(money)), end=' ')
    # print(binarySearch(money, price * 2, left=0, right=len(money)), end=' ')
