# Две фишки (из яндекс контеста)
a = int(input())
s = str(input())
b = int(input())  # искомое, сумма должна быть равна этому числу

# Ленивый алгоритм
# 2.655s | 4.00Mb  - Две фишки
# 1.09s  | 12.69Mb - Две фишки - 2

nums = list(map(int, s.split()))
res = []
ch = False

# for i in range(0, len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == b:
#             print(nums[i], nums[j])
#             ch = True
#             break
#     if ch:
#         break
#     pass
# if not ch:
#     print(None)

# ------------------------------------------------------------------------
# Оптимизированный алгоритм: метод двух указателей
# 56ms | 3.98Mb    - Две фишки
# 134ms  | 12.58Mb - Две фишки - 2

nums.sort()
left = 0
right = len(nums) - 1
while left < right:
    current_sum = nums[left] + nums[right]
    if current_sum == b:
        print(nums[left], nums[right])
        ch = True
        break
    if current_sum < b:
        left += 1
    else:
        right -= 1

if not ch:
    print(None)

# ------------------------------------------------------------------------
# Оптимизированный алгоритм 2: с применением структуры данных поиска
# 50ms  | 4.00Mb  - Две фишки
# 115ms | 13.47Mb - Две фишки - 2

prev = set()
for i in nums:
    y = b - i
    if y in prev:
        print(y, i)
        ch = True
        break
    else:
        prev.add(i)

if not ch:
    print(None)
