a = input().split(",")
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
i = len(a)-1
while i>=0:
    print(a[i],end=" ")
    i=i-1