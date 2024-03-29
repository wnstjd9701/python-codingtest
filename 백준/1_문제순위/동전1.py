# 백준 2293번 문제 - 동전 1
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in coin:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[k])