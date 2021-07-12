import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = list(input().rstrip().split(" "))

result = abs(n - 100)

for num in range(1000001):
    number = list(str(num))
    check = 0
    for i in number:
        if i in s: check =1
    if check == 0:
        result = min(result, len(str(num)) + abs(num - n))

print(result)

