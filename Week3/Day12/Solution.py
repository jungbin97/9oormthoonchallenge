# ------------------------------------
# dfs
# 상하좌우 서로 연결되어있는 집의 그룹 개수 구하기

# 실패 : testcase 4, 10, 11, 12, 13, 14, 19, 22 
# ------------------------------------
import sys
input = sys.stdin.readline

# 행,열 크기
N = int(input().rstrip())
M = []
visited = [[0]*N for _ in range(N)]

cnt = 0

for _ in range(N):
    M.append(list(map(int, input().rstrip().split())))

def dfs(x, y):
    # 방문 처리
    visited[x][y] = 1
    
    # 상하 좌우
    for dx, dy in [(-1,0), (1,0),(0,-1),(0,1)]:
        nx = x + dx
        ny = y + dy

        if 0<=nx<N and 0 <= ny<N and M[nx][ny]== 1 and visited[nx][ny] == 0:
            dfs(nx, ny) 
            

for i in range(N):
    for j in range(N):
        # 1이고 아직 방문하지 않았다면 dfs 돌리기
        if M[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)


# ------------------------------------
# BFS 통과 코드 
# ------------------------------------
from collections import deque
import sys
input = sys.stdin.readline

# 행,열 크기
N = int(input().rstrip())
M = []
visited = [[0]*N for _ in range(N)]

cnt = 0

for _ in range(N):
    M.append(list(map(int, input().rstrip().split())))

def bfs(r, c):
    # 큐 생성
    q = deque([(r,c)])

    # 방문처리
    visited[r][c] = 1

    while q:
        r, c = q.popleft()

        # 상하좌우
        for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
            nx = r + dx
            ny = c + dy

            # 범위 체크
            if 0<= nx <N and 0 <= ny < N and M[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

for i in range(N):
    for j in range(N):
        if M[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
            
print(cnt)