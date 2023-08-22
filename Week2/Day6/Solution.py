#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

p = set()
temp = []
for i in range(1, n-1):
    for j in range(i+1, n):
        s1, s2, s3 = s[:i], s[i:j], s[j:]
        p.add(s1)
        p.add(s2)
        p.add(s3)
        temp.append((s1, s2, s3))

p = sorted(list(p))

result = 0
for i in temp:
    sum1 = p.index(i[0]) + p.index(i[1]) + p.index(i[2]) + 3
    result = max(result, sum1)
print(result)