#------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------
import sys

input = sys.stdin.readline


N, K = map(int, input().rstrip().split())

# 맵 입력 초기화
M = [list(map(int, input().split())) for _ in range(N)]

result = 0
for x in range(N):
    for y in range(N):
        # 구름이 없는 곳이면
        if M[x][y] == 0:
            count = 0
            # 상 하 좌 우 오른쪽아래, 오른쪽 위, 왼쪽 위, 왼쪽 아래
            for dx, dy in [(-1,0), (1,0), (0, -1), (0,1), (1,1),(-1,1),(-1,-1),(1, -1)]:
                nx = x + dx
                ny = y + dy
                # 인덱스 범위 체크, 구름이 있는지 체크
                if 0<= nx < N and 0<= ny < N and M[nx][ny] == 1:
                    count += 1

            if count == K:
                result += 1

print(result)