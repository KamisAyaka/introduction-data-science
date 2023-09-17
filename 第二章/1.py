def maxProductList(n):
    dp = [0] * (n + 1)
    result = [[] for _ in range(n + 1)]
    dp[1] = 1
    result[1] = [1]
    for i in range(2, n + 1):
        max_product = 0
        max_j = 0
        for j in range(1, i // 2 + 1):
            current_product = dp[j] * dp[i - j]
            if current_product > max_product:
                max_product = current_product
                max_j = j
        if max_product > i:
            dp[i] = max_product
            result[i] = result[max_j] + result[i - max_j]
        else:
            dp[i] = i
            result[i] = [i]
    return result[n]

n = 9
result_list = maxProductList(n)
print("正整数列表:", result_list)