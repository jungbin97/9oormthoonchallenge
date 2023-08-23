# 통증 수치
N = int(input())

cnt = 0
while N:
    if N>= 14:
        cnt += 1
        N -= 14
    elif N>= 7:
        cnt += 1
        N -= 7
    else:
        cnt += N        
        N = 0


print(cnt)