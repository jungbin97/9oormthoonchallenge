# -----------------------------------------------
# union - find 사용 (testCase - 10~23, 26~31, 33~37 시간초과)
# parent[x] = find(parent, parnet[x])로 재귀식을 최적화를 해주었는데도 시간 초과;;
# 이리 저리 삽질해봐도 시간 초과뜨길래 포기하고 bfs로 풀었다.
# -----------------------------------------------
# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     a = find(parent, a)
#     b = find(parent, b)
    
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# N, M = map(int, input().split())

# # 부모 테이블 초기화
# parent = [i for i in range(N+1)]
# edges = []

# for _ in range(M):
#     s, e = map(int, input().split())
#     edges.append((s, e))

# # 양방향 있는것들만 체크해서 union 해줌.
# for s, e in edges:
#     if (e, s) in edges:
#         union(parent, s, e)

# answer = set()
# for i in range(1, N+1):
#     answer.add(find(parent, i))

# print(len(answer))

# -----------------------------------------------
# BFS 풀이
# -----------------------------------------------
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

def bfs(start, check):
    check[start] = True
    q = deque([start])
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            # 방문했는지 체크 and 현재 노드 다음노드 양방향 연결인지 체크
            if not check[next_node] and node in graph[next_node]:
                q.append(next_node)
                check[next_node] = True

cnt = 0
check = [False] *(N+1)
for i in range(1, N+1):
    if not check[i]:
        bfs(i, check)
        cnt += 1

print(cnt)