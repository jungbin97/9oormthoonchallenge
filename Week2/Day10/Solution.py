n = int(input())

gx, gy = map(lambda x: x - 1, map(int, input().split()))

px, py = map(lambda x: x - 1, map(int, input().split()))

board_arr = [list(input().split()) for _ in range(n)]

direction_mapper = {"U": 0, "D": 1, "R": 2, "L": 3}

def simulate_movement(x, y):
    visit_arr = [[0 for _ in range(n)] for _ in range(n)]
    dx_arr = [-1, 1, 0, 0]
    dy_arr = [0, 0, 1, -1]
    
    score = 0

    while not visit_arr[x][y]:
        visit_arr[x][y] = 1
        score += 1
        
        command = board_arr[x][y]
        count, direction = int(command[:-1]), direction_mapper[command[-1]]
        
        for _ in range(count):
            x = (x + dx_arr[direction]) % n
            y = (y + dy_arr[direction]) % n
            
            if visit_arr[x][y]:
                return score
    return score

goorm_score = simulate_movement(gx, gy)
player_score = simulate_movement(px, py)

if goorm_score > player_score:
    print("goorm", goorm_score)
else:
    print("player", player_score)
