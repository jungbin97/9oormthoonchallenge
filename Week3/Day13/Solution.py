from collections import deque
import sys
input = sys.stdin.readline

# 행,열 크기
N, K = map(int, input().split())
M = []
visited = [[0]*N for _ in range(N)]

cnt = [0]*31

for _ in range(N):
    M.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            q = deque([(i, j)])

            # 방문처리
            visited[i][j] = 1
            temp_cnt = 1
            while q:
                x, y = q.popleft()


                # 상하좌우 체크
                for dx, dy in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    nx = x+dx
                    ny = y+dy

                    # 범위 체크
                    if 0<= nx < N and 0<= ny < N and M[nx][ny] == M[x][y] and visited[nx][ny] == 0:
                        temp_cnt += 1
                        q.append((nx, ny))
                        visited[nx][ny] = 1

            if temp_cnt >= K:
                cnt[M[i][j]] += 1

# 가장 많은 단지가있는 경우 Mrc가 더큰 건물 유형을 뽑음(cnt 리스트 뒤에서 부터 탐색)            
print(len(cnt)-1 -  cnt[::-1].index(max(cnt)))