# J. Пузырёк

def bubble_sort(number, source_array):
    flag = 1
    for num in range(number - 1):
        for num_2 in range(0, number-num-1):
            if source_array[num_2] > source_array[num_2+1]:
                source_array[num_2], source_array[num_2+1] = source_array[num_2+1], source_array[num_2]
                flag = 1
        if flag == 1:
            for num_3 in source_array:
                print(num_3, end=' ')
            print('')
            flag = 0


if __name__ == '__main__':
    number = int(input())
    source_array = [int(num) for num in input().split(' ')]
    bubble_sort(number, source_array)
