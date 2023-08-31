import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 노드 방문 체크
visited = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    # 양방향 간선 연결
    graph[a].append(b)
    graph[b].append(a)

# 작은 것 부터 (오름차순)
for i in range(1, N+1):
    graph[i].sort()

visited[K] = 1
cnt = 1

for _ in range(N):
    for next_node in graph[K]:
        if visited[next_node] == 0:
            visited[next_node] = 1
            K = next_node
            cnt += 1
            break

print(cnt, K)



# ----------------------------------------------
# 인접행렬방식
# ----------------------------------------------
# import sys

# n, m, k = map(int, sys.stdin.readline().split())

# arr = [[0 for i in range(n + 1)] for j in range(n + 1)]

# for i in range(m):
#     node1, node2 = map(int, sys.stdin.readline().split())
#     arr[node1][node2] = 1
#     arr[node2][node1] = 1

# visited = set()
# visited.add(k)

# count = 1
# while True:
#     for j in range(1, n + 1):
#         if arr[k][j] == 1:
#             if j not in visited:
#                 visited.add(j)
#                 count += 1

#                 k = j
#                 break
#     else:
#         break

# print(count, k)