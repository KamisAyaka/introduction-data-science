import math

binary = ""
a = float(input())
b = math.modf(a)
c = b[0]
binary +=str(int(b[1]))
binary +="."
#二进制移位操作，*2等价于左移一位
while c > 0 :
    c *= 2
    binary += str(int(c))
    c -= int(c)
print(binary)