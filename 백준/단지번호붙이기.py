# 백준 2667번 문제 - 단지 번호 붙이기
n = int(input())
graph = []
num = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n :
        return False 

    if graph[x][y] == 1:
        global cnt 
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in num:
    print(i)

# end