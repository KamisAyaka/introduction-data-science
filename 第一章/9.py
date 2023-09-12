a = input()
a = list(a)
flag = 0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        flag = 1
        break
print(flag)