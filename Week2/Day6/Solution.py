import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

p = set()
for i in range(1, n-1):
    for j in range(i+1, n):
        s1, s2, s3 = s[:i], s[i:j], s[j:]
        p.add(s1)
        p.add(s2)
        p.add(s3)

p = sorted(list(p))

result = 0
for i in range(1, n-1):
    for j in range(i+1, n):
        s1, s2, s3 = s[:i], s[i:j], s[j:]
        sum1 = p.index(s1) + p.index(s2) + p.index(s3) + 3
        result = max(result, sum1)
print(result)