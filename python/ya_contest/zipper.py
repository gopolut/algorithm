'''
Даны два массива чисел длины n. Составьте из них один массив длины 2n,
в котором числа из входных массивов чередуются (первый — второй — первый — второй — ...).
При этом относительный порядок следования чисел из одного массива должен быть сохранён.
'''
l = int(input())
n = str(input())
k = str(input())

nl = list(map(str, n.split()))
kl = list(map(str, k.split()))

new = []
for i in range(l):
    new.append(nl[i])
    new.append(kl[i])

s = ' '.join(new)
print(s)
