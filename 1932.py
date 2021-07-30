import sys
input = sys.stdin.readline

N = int(input())
tree = [list(map(int,input().split(" "))) for _ in range(N)]
if N>=2:
    tree[1][0] += tree[0][0]
    tree[1][1] += tree[0][0]
if N>=3:
    for i in range(2,N):
        for j in range(len(tree[i])):
            if j==0: tree[i][j] +=tree[i-1][j]
            elif j==len(tree[i])-1: tree[i][j] += tree[i-1][j-1]
            else: tree[i][j] = max(tree[i][j]+tree[i-1][j-1], tree[i][j]+tree[i-1][j])

print(max(tree[N-1]))

