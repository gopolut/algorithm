# из теории ЯП.

# Напротив каждой позиции она написала число — сколько раз нужная буква (C или G)
# встретилась от начала строки и до текущей позиции (не включая её саму) —
# это называется «накопительная сумма» (англ. cumulative sum).

sequence = 'CCATGATC'
right = 7
left = 0

cumulative_sums = [0]
cg_count = 0

for position in range(0, len(sequence)):
    if (sequence[position] == 'C') or (sequence[position] == 'G'):
        cg_count += 1
    cumulative_sums.append(cg_count)

print(cumulative_sums)
print(cumulative_sums[right + 1] - cumulative_sums[left])

