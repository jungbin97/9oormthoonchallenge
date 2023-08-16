import sys

input = sys.stdin.readline

n = int(input().rstrip())
t, m = map(int, input().rstrip().split())

# 기능 개발 시간 입력
for _ in range(n):
	m += int(input().rstrip())

# 분으로 변환
min_sum = ((t*60)+m)

print("{} {}".format((min_sum//60)%24, min_sum%60))