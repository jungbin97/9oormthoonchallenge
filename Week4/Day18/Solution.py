import sys
input = sys.stdin.readline

# 가로선, 세로선 그리는 함수
def draw_line(r,c,d):
    dx, dy = direction[d]
    while True:    
        # 인덱스 범위 넘어가면 반복문 탈출
        if r < 0 or c<0 or r >= n or c >= n:
            break
        
        if d == 'L' or d == 'R':
            graph[r][c][0] += 1
        elif d == 'U' or d == 'D':
            graph[r][c][1] += 1

        r += dx
        c += dy
            
# n행열, m 직선 개수
n, m = map(int, input().split())

direction = {"U": (-1,0), "D":(1,0), "L":(0,-1), "R":(0,1)}

#(가로, 세로) 값 저장
graph = [[[0,0] for _ in range(n)] for _ in range(n)]

# 반직선 입력 받기
for _ in range(m):
    # 행, 열 좌표, 방향
    r, c, d = map(str, input().split())

    r = int(r) -1
    c = int(c) -1

    # 그래프에 가로 개수, 세로 개수 저장함!
    draw_line(r, c, d)

# 출력
cnt = 0
for i in range(n):
    for j in range(n):
       cnt +=  graph[i][j][0] * graph[i][j][1]

print(cnt)