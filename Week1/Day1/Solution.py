import sys

input = sys.stdin.readline
w, r = map(int, input().rstrip().split())
print(int(w*(1+r/30)))