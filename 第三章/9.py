a = input().split(",")
b = list(1 for i in range(len(a)))
for i in range(0,len(a)) :
    for j in range(0,i):
       b[i] *= int(a[j])
    for j in range(i+1,len(a)):
       b[i] *= int(a[j])
print(b)