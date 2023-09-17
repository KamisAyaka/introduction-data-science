#蒙特卡罗方法
import  random
n = 100000
i = 0.0
for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x ** 2 + y ** 2
    if distance <= 1:
           i += 1
print(i / 25000)

#级数方法
i = 0
pai = 0
for i in range(n):
    pai += (-1)**i /(2*i+1)
print(4*pai)