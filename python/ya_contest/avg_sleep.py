sec = int(input())
time = str(input())
k = int(input())

time = list(map(int, time.split()))
res = []

# ленивый алгоритм: 1.09s | 14.20Mb (TL)
for beg_i in range(0, len(time)-k+1):
    end_i = beg_i + k
    cursum = 0
    for x in time[beg_i:end_i]:
        cursum += x
    avg = cursum/k
    res.append(avg)

# Оптимизированный 'ленивый' алгоритм - "метод двух указателей":
# 178ms | 14.83Mb
cursum = sum(time[0:k])
res.append(cursum/k)

for i in range(0, len(time) - k):
    cursum -= time[i]
    cursum += time[i+k]
    avg = cursum/k
    res.append(avg)

print(res)
print(' '.join(map(str, res)))

# ====================================
number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')
