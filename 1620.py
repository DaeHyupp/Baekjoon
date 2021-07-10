import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dic = {}
for i in range(1, N+1):
    name = input().rstrip()
    dic[name] = str(i)
    dic[str(i)] = name

for _ in range(M):
    print(dic[input().rstrip()])
