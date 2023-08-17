#------------------------------------------------------------------------------------
# 시간 복잡도 O(n)
# 1차 풀이 선형 탐색
#------------------------------------------------------------------------------------
import sys

input = sys.stdin.readline

n = int(input().rstrip())

# 맛 정도 리스트 초기화
tastes_list = list(map(int , input().split()))

def taste_fnc():
    global n, tastes_list
    # 최고 맛도리 인덱스 찾기 O(2n) => O(n)
    max_taste_idx = tastes_list.index(max(tastes_list))

    for i in range(max_taste_idx, n-1):
        if tastes_list[i] < tastes_list[i+1]:
            return 0
        
    for i in range(max_taste_idx -1, 0, -1):
        if tastes_list[i] < tastes_list[i-1]:
            return 0
        
    return sum(tastes_list)


print(taste_fnc())
