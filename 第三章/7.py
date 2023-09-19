n = int(input())
m = int(input())
while m:
    n,m = m,n%m
print(n)