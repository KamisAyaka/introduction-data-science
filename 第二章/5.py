c = int(input())
g = c/2
i = 0
while abs(g**2-c) > 0.000000000001:
     g = (g + c/g) /2
     i += 1
     if abs(g**2-c) < 0.000000000001:
         print(i,g)
         break