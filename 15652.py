import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split(" "))

arr = []

def dfs():
    if len(arr)==M: print(" ".join(map(str,arr)));return
    for i in range(1,N+1):
        if len(arr)==0: arr.append(i)
        elif i >= arr[-1]: arr.append(i)
        else: continue
        dfs()
        arr.pop()

dfs()

