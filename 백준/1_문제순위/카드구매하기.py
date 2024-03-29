# 백준 11052번 문제 - 카드 구매하기
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])