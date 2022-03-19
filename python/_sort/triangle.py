# F. Периметр треугольника

def triangle(cuts):
    for i in range(len(cuts) - 2):
        if cuts[i] < cuts[i + 1] + cuts[i + 2]:
            print(cuts[i] + cuts[i + 1] + cuts[i + 2])
            break
        else:
            i += 1


if __name__ == '__main__':
    number = int(input())
    cuts = sorted([int(x) for x in input().split()], reverse=True)

    triangle(cuts)
