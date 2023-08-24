#--------------------------------------------------------
# 땅상태가 0 -> 1 -> 2
# 땅상태가 @ -> 2 -> 4
#--------------------------------------------------------
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# 맵초기화
graph = []
# 
counts = [[0]*n for _ in range(n)]

for i in range(n):
    graph.append(input().strip().split())     # 문자열로 받음 => @, # 값 때문에

# 폭탄 투하 횟수k 만큼 입력받음
for i in range(k):
    x, y = map(int , input().rstrip().split())
    x-=1
    y-=1

    # 가운데, 상, 하, 좌, 우
    for dx, dy in [(0,0),(-1,0), (1,0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
				# 폭탄 투하 count 처리부분
        if 0<= nx < n and 0 <= ny <n:
            if graph[nx][ny] == '@':
                counts[nx][ny] += 2
            else:
                counts[nx][ny] += 1
                if graph[nx][ny] == '#':
                    counts[nx][ny] -= 1

print(max(map(max, counts)))