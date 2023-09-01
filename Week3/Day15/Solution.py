import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = []

result = 0
for _ in range(N):
    # 각 조각 포만감, 과일 가격, 포만감
    P, C = map(int,input().split())
    arr.append((C//P, P))

# 각 조각 포만감이 높은순, 같으면 가격이 낮은 순
arr.sort(key= lambda x:(-x[0], x[1]))

# 시간 복잡도 O(N^2)에서 O(N)으로 개선
# ---------------------------------------
# for i in range(N):
#     for j in range(arr[i][1]):
#         if K == 0:
#             break;

#         K -= 1
#         result += arr[i][0]
# ---------------------------------------

for i in range(N):
    # 각 조각의 포만감 * (해당 과일을 최대로 먹을 수 있는 조각 수)를 결과에 더함
    max_pieces = min(K, arr[i][1])
    result += arr[i][0] * max_pieces
    K -= max_pieces
    
    if K == 0:
        break        

print(result)