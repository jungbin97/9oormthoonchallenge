import sys

input = sys.stdin.readline

t = int(input().rstrip())
total = 0
def calculator(operator,a,b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a//b
    
for _ in range(t):
    str = input().split() 

    a = int(str[0])
    b = int(str[2])
    operator = str[1]

    total += calculator(operator, a, b)

print(total)