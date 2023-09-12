a = input().split(",")
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if int(a[j]) > int(a[j + 1]):
            a[j],a[j+1]=a[j+1],a[j]
for i in range(0, 3):
    print(a[i],end=" ")
