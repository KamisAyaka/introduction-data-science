def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"移动盘子 {n} 从 {source} 到 {target}")
        return
    hanoi(n-1, source, target, auxiliary)
    print(f"移动盘子 {n} 从 {source} 到 {target}")
    hanoi(n-1, auxiliary, source, target)

hanoi(3, 'A', 'B', 'C')
