A = [["狼", 1], ["羊", 1], ["菜", 1]]
B = [["狼", 0], ["羊", 0], ["菜", 0]]
size = len(A)
count = 0
number = -1


def judge(A):
    if A[1][1] == 1 and A[0][1] + A[2][1] == 1:
        return False
    else:
        return True


def A_to_B():
    global number
    global count
    for i in range(size):
        if A[i][1] == 1 and i != number:
            A[i][1] -= 1
            if judge(A):
                B[i][1] += 1
                number = i
                print("%s ,A—>B" % A[i][0])
                count += 1
                break
            else:
                A[i][1] += 1
                continue
        else:
            continue


def B_to_A():
    global number
    global count
    if not judge(B):
        for j in range(size):
            if B[j][1] == 1 and j != number:
                B[j][1] -= 1
                A[j][1] += 1
                number = j
                print("%s ,B—>A" % B[j][0])
                count += 1
                break
    else:
        if B[0][1] + B[1][1] + B[2][1] == 3:
            print("任务完成")
        else:
            print("人 ,B->A")
            count += 1

def shore(A):
    list1 = []
    for i in range(size):
        if A[i][1] == 1:
            list1.append(A[i][0])
    return list1


def sucess():
    if B[0][1] + B[1][1] + B[2][1] == 3:
        return True
    else:
        return False


while 1:
    print("A岸上有", shore(A))
    print("B岸上有", shore(B))
    A_to_B()
    print("A岸上有", shore(A))
    print("B岸上有", shore(B))
    B_to_A()

    if sucess():
        print("这个程序需要", count, "步")
        break
