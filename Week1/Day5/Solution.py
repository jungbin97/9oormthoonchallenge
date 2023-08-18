#------------------------------------------------------------------------------------
# lambda 식에서 음수로 정렬하면 내림차순인 이유!
# [3, 2, 1]를 오름차순 => [1, 2, 3]
# 음수 취하면 [-3, -2 ,-1]을 오름차순 => [-3, -2, -1]
# 따라서 원래의 값으로 돌리면 [3, 2, 1]같이 내림차순으로 정렬됨.
#------------------------------------------------------------------------------------
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

# 첫번째 정렬
sorted_arr = sorted(arr, key=lambda x: (-(bin(x).count('1')), -x))

print(sorted_arr[k-1])