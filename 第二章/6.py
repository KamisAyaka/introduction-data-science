c = int(input())
g = c/2
i = 0
while abs(g**3-c) > 0.00000000001:
     g = (2 * g+ c/(g**2))/3
     i += 1
     if abs(g**3-c) < 0.000000000001:
         print(i,g)
         break