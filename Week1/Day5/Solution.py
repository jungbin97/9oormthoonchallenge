#------------------------------------------------------------------------------------
# 
#------------------------------------------------------------------------------------
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))

# 첫번째 정렬
sorted_arr = sorted(arr, key=lambda x: (-(bin(x).count('1')), -x))

print(sorted_arr[k-1])