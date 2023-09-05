from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 인접리스트로 입력 받기(1 ~ N까지)
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

def bfs(node):
    visited[node] = True
    q = deque([node])
    component = [node]
    edges = 0

    while q:
        current = q.popleft()
        for next_node in graph[current]:
            # edges += 1
            if not visited[next_node]:
                # edges += 1  # 두번 세는거 방지
                visited[next_node] = True
                q.append(next_node)
                component.append(next_node)
    return component, edges//2
    # return component, edges


components = []
for i in range(1, N+1):
    if not visited[i]:
        comp, edges = bfs(i)
        components.append((comp, edges))

# 가장 밀도(m/n) 내림차순, 컴퓨터의 수(n) 오름차순, 작은 번호 노드 오름차순
components = sorted(components , key=lambda x: (-x[1]/len(x[0]), len(x[0]), min(x[0])))

# 컴포넌트 오름차순으로 출력
print(*sorted(components[0][0]))

