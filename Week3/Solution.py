# -------------------------------------------------------------------------
# A와 B는 배수관계가 아니다. => 그리디 방식으로 해결 할 수 없다 => DP해결방법을 고려해볼까?
# -------------------------------------------------------------------------
import sys

input = sys.stdin.readline

N = int(input())

#dp 테이블 초기화
dp = [float('inf')] * ((10**6)+1)
Ap, Bp = map(int, input().split())

dp[0] = 0
for i in range(1, N+1):
    # dp[]테이블 인덱스 체크
    if i - Ap >= 0:
        dp[i] = min(dp[i], dp[i-Ap]+1)
    if i - Bp >= 0:
        dp[i] = min(dp[i], dp[i-Bp]+1)

if dp[N] == float('inf'):
    print(-1)
else:
    print(dp[N])
    
# -------------------------------------------------------------------------
# top-down방식 시간 초과(test Case 5~24번)
# 재귀 + Dp 방식으로 풀어보려고 했으나 시간 초과로 Fail
# 식을 입력하면 계산에 대한 내용은 컴퓨터에게 맡기니 코드는 보기 좋으나 stack overflow 때문에
# 코딩 테스트에서는 최대한 지양해야겠다...
# -------------------------------------------------------------------------
import math
import sys
# 입력 받기
N = int(input())
Ap, Bp = map(int, input().split())
dp = [float('inf')] * (10**6+1)

def solve(pain):
    if pain == 0:
        return 0
    if pain < 0:
        return float('inf')
    
    dp[pain] = min(solve(pain - Ap), solve(pain - Bp)) + 1
    return dp[pain]

result = solve(N)
if result == float('inf'):
    print(-1)
else:
    print(result)