import sys

input = sys.stdin.readline

# 게임을 시뮬레이션할 함수를 선언
def play(sy, sx, N):
    # 현재 위치를 담을 y, x를 선언합니다.
    y, x = sy, sx

    # 방문 배열을 선언하고, 시작 좌표에 대해 방문처리
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1

    # 게임의 종료 조건을 충족할 때까지 시뮬레이션 돌리기 위해
    notEnd = True

    while notEnd:
        # 현재 위치에서 count값과 방향을 불러옴
        cnt = count[y][x]
        dy, dx = command[y][x]

        # cnt만큼 dy, dx를 이용해 한방향으로 이동
        for _ in range(cnt):
            y = (y + dy) % N
            x = (x + dx) % N

            # 범위 처리를 완료, 만약 (y, x)위치를 방문 했다면 게임 종료
            if visited[y][x]:
                notEnd = False
                break

            # 방문하지 않았다면 방문 처리
            visited[y][x] = 1
        
        # while문이 종료되면 여기로 올 것, 
    return sum([sum(i) for i in visited])

N = int(input())

# 구름이 말 좌표
rg, cg = map(int, input().split())

# 플레이어 말 좌표
rp, cp = map(int, input().split())
rg -= 1
cg -= 1
rp -= 1
cp -= 1

count_commands = [list(input().split()) for _ in range(N)]

count = [[0] * N for _ in range(N)]
command = [[None]*N for _ in range(N)]

direction = {"L": [0,-1], "R":[0, 1], "U":[-1, 0], "D":[1, 0]}

for i in range(N):
    for j in range(N):
        temp = count_commands[i][j]
        
        #문자열 처음부터, 오른쪽 맨 끝 바로 앞글자까지 잘라서 정수 변환
        count[i][j] = int(temp[:-1])

        # 문자열의 오른쪽 끝 글자를 잘라서 direction의 key 값으로 사용
        key = temp[-1]

        # command의 각 원소에 대해 dy, dx를 저장합니다.
        command[i][j] = direction[key]

socre_G = play(rg, cg, N)
socre_P = play(rp, cp, N)

if socre_G > socre_P:
    print("goorm", socre_G)
else:
    print("player", socre_P)