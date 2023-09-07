import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, s, e, repair_city):
    # 시작 도시나 끝 도시가 공사중이라면 - 1
    if s == repair_city or e == repair_city:
        return -1

    # 공사할 도시가 매일 바뀌기 떄문에 내부에 visited 생성함
    visited = [False] * (n+1)

    # 도시와 방문한 도시 수
    q = deque([(s, 1)])
    visited[s] = True

    while q:
        city, cnt = q.popleft()

        # 목적지에 도달했는지 확인
        if city == e:
            return cnt
        
        for next_city in graph[city]:
            # 아직 방문하지 않고, 수리중인 도시가 아니라면 큐에 삽입
            if not visited[next_city] and next_city != repair_city:
                visited[next_city] = True
                q.append((next_city, cnt+1))

    # 모두 순회해도 목적지에 도달할수 없는 경우
    return -1

# 도시수, 도로수, 출발노드, 도착 노드
n, m, s, e = map(int, input().split())

graph = {i : [] for i in range(1, n+1)}

# 간선 입력받기
for _ in range(m):
    u, v = map(int,input().split())
    # 도시 양방향으로 연결
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    print(bfs(graph, s, e, i))
