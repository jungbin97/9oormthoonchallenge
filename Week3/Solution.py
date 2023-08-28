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