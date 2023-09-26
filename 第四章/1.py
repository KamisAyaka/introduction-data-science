a = int(input())
if a % 2 == 0:
    print("a不是质数")
else:
    flag = 0
    for i in range(3, a, 2):
        if a % i == 0:
            flag = 1
            break
    if flag == 0:
        print("a是质数")
    else:
        print("a不是质数")
