# 재귀 함수를 이용한 조합 구현
arr = [1, 2, 3]

# 조합 저장 배열
comb = []

def combinations(temp, start, end):
    # 만약 temp의 길이가 2이면 모두 고른것이므로 comb에 추가하고 리턴함
    if len(temp) == 2:
        comb.append(temp)
        return

    # 선택한 공백을 추가하고 재귀를 호출합니다.
    for i in range(start, end):
        combinations(temp+[arr[i]], i+1, end)

combinations([], 0, len(arr))
print(comb)