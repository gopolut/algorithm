# visitors = [0,2,3,2,0,4,1,1,2]
# entries_by_visitor = [0] * 5 # массив из 5 элементов (кол-во поездок пассажиров)
# best_visitor = 0

# for visitor in visitors:
#     entries_by_visitor[visitor] += 1 # каждый раз прибавляем +1 каждому пассажиру, на котором в данный момент находимся в цикле
#     # пассажир №    :  1  2  3  4  5
#     # кол-во поездок: [0, 0, 0, 0, 0]
#     if entries_by_visitor[visitor] > entries_by_visitor[best_visitor]:
#         best_visitor = visitor

# print(best_visitor)

# -----------------------------------------------------------------------
# Сравнение 2-х яблок
N = [1.5, 1.7, 2.0, 1.9, 1.8, 1.4]
ap1 = 0
ap2 = 0
dif = abs(N[0] - N[1])

for i in range(0, len(N)-1):
    for j in range(0, len(N)):
        a = abs(N[i] - N[j])
        if i != j:
            if abs(N[i] - N[j]) < dif: # and i != j:
                dif = abs(N[i] - N[j])
                ap1 = N[i]
                ap2 = N[j]

print(dif)
print(ap1, ap2)
