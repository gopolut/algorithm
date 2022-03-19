# N. Клумбы
# ----------

# def flower(array):
#     new_array = []
#     for i in range(len(array)-1):
#         if array[i+1][0] <= array[i][1]:  # and array[i+1][1] > array[i][1]:
#             # конец нового отрезка
#             # конец отрезка от i[1][1]
#             if array[i][1] > array[i+1][1]:
#                 array[i+1] = [array[i][0], array[i][1]]
#                 array[i] = None
#                 new_array.append(array[i+1])
#             # конец отрезка от [i+1][1]
#             else:
#                 array[i+1] = [array[i][0], array[i+1][1]]
#                 array[i] = None
#                 new_array.append(array[i+1])
#         else:
#             new_array.append(array[i+1])
#     print(array)
#     for j in array:
#         if j is not None:
#             print(j, sep='\n')

def flower(intervals):
    out = []
    output = ''
    for i in sorted(intervals, key=lambda i: i[0]):
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += i,
    # return out
    for i in out:
        output += ' '.join(str(j) for j in i) + '\n'
    print(output.strip())


# flower([[2, 3], [6, 10], [7, 8], [7, 8]])
# flower([[2, 3], [3, 4], [3, 4], [5, 6]])
# flower([[1, 3], [2, 4], [3, 5], [4, 6], [5, 6], [7, 10]])


# def read_input() -> Tuple[List[List[str]], int]:
#     keys_count = int(input())
#     trainer = []
#     for i in range(keys_count):
#         trainer.append(list(map(int, input().split(' '))))

#     return keys_count, trainer


# def main():
#     keys_count, trainer = read_input()
#     flower(trainer)


if __name__ == '__main__':

    keys_count = int(input())
    cuts = []
    for i in range(keys_count):
        cuts.append(list(map(int, input().split(' '))))
    flower(cuts)
