import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
parent = [i for i in range(G + 1)]
planes = list(int(input()) for _ in range(P))

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

ans = 0
for plane in planes:
    docking = find(plane)
    if docking == 0: break
    parent[docking] = parent[docking - 1]
    ans += 1
print(ans)

#ref https://mygumi.tistory.com/246
