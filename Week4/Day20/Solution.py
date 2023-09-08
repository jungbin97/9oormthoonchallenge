import sys
from collections import deque
input = sys.stdin.readline

n, k, q = map(int,input().split())

graph = [list(input().strip()) for _ in range(n)]

# 삽입할 문자 입력 받기
inputStr = [list(input().split()) for _ in range(q)]


def bfs(x, y, graph):
    global n
    visited = [[False]*n for _ in range(n)]
    connectElments = [(x, y)]
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        i, j = q.popleft()
        # 상하 좌우 이동
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = i + dx, j + dy
            # 인덱스 범위 체크 및 방문체크 및 같은 문자인지체크
            if 0<= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                visited[nx][ny] = True
                q.append((nx, ny))
                connectElments.append((nx,ny))
    return connectElments




for x, y, d in inputStr:
    x, y = int(x) - 1, int(y) - 1
    # x, y칸은 . 문자가 적힌 칸을 보장하기 때문에 그냥 삽입
    graph[x][y] = d

    # 삽입된 인접한 요소듦만 체크
    connectElments = bfs(x, y, graph)
    if len(connectElments) >= k:
        for i, j in connectElments:
            graph[i][j] = "."


for row in graph:
    print(''.join(row))
