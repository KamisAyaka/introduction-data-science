c = int(input())
g = c/2
i = 0
while abs(g**2-c) > 0.001:
     g += 0.0001
     i += 1
     if abs(g**2-c) < 0.001 :
         print(i,g)
         break