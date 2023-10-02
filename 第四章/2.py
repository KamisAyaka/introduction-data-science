import time

# 记录开始时间
start_time = time.time()

# 执行需要计时的代码
# 例如：计算一个大型任务的执行时间
for _ in range(1000000):
    _ = 2 * 2

# 记录结束时间
end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time

print(f"程序执行时间：{execution_time} 秒")
