def key(first, second):
    i = 0
    while i <= len(second) - 1:
        try:
            if second[int(i)] < first[int(i)]:
                return False
            elif second[int(i)] == first[int(i)]:
                i += 1
            else:
                return True
        except IndexError:
            if second[int(i)] > first[int(0)]:
                return True
            return False
    if len(second) < len(first):
        if first[int(i)] > second[int(0)]:
            return False
        return True
    return False


def big(first, second):
    if len(first) > len(second):
        return first
    return second


def little(first, second):
    if len(first) > len(second):
        return second
    return first


def key2(first, second):
    i = 0
    for i in range(len(second) - 1):
        for j in range(len(first) - 1):
            if second[i] < first[i]:
                return False
            j += 1


def big_number(nums, number):
    for i in range(1, len(nums)-1):
        insert = nums[i]
        for j in range(i, 0, -1):
            # if nums[j - 1] < insert:
            # if number(nums[j - 1]) <= number(insert):
            if number(nums[j - 1], insert):
                nums[j], nums[j - 1] = nums[j - 1], insert
            j -= 1
    print(nums)
    return ''.join(map(str, nums))


if __name__ == '__main__':
    count = int(input())
    array = [str(num) for num in input().split(' ')]
    print(big_number(array, key))
