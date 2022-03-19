#  Python 2.7
num1, num2 = (open("input.txt", "r").read()).split()
resu = open("output.txt","w")
resu.write(str(int(num1) + int(num2)))

# Python 3.6
reader = open('input.txt', 'r')
a, b = [int(n) for n in reader.readline().split(" ")]
reader.close()

writer = open('output.txt', 'w')
writer.write("%d" % (a+b))
writer.close()
