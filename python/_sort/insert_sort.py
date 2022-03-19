# Сортировка вставкой

def insert_sort(nums):
    for i in range(1, len(nums)):
        insert_number = nums[i]

        for j in range(i, 0, -1):
            if nums[j - 1] > insert_number:
                # Присвоение значения по колхозному
                # nums[j] = nums[j - 1]
                # nums[j - 1] = insert_number

                # Присвоение значения по-питоновски
                nums[j], nums[j - 1] = nums[j - 1], insert_number
            j -= 1
    return nums


if __name__ == '__main__':
    array = [int(num) for num in input().strip()]
    print(insert_sort(array))
