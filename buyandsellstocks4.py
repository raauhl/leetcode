def max_profit(k, prices):
    n = len(prices)
    cache = [[0] * (n+1) for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, n+1):

            for day in range(j):
                curr_profit = max(curr_profit, prices[j] - prices[day] + cache[i-1][day])
            
            cache[i][j] = max(curr_profit, cache[i][j-1])

    return cache[k+1][n+1]
