import sys
input = sys.stdin.readline
N=int(input())
mat = [list(map(int, input().rstrip().split(" "))) for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        mat[i][j] += mat[j][i]
        mat[j][i] = 0

def backtrack(i):
    global sheet,arr
    sheet.append(i)
    if len(sheet) == N//2:
        ans = 0
        for p in range(len(sheet)-1):
            for q in range(p+1,len(sheet)):
                ans += mat[sheet[p]][sheet[q]]
        arr.append(ans)
        return                
    for j in range(i+1,N):
        backtrack(j)
        sheet.pop(-1)
    
arr = []
for i in range(N):
    sheet = []
    backtrack(i)
real = 10000000
for i in range(len(arr)//2):
    real=min(real,abs(arr[i]-arr[len(arr)-1-i]))
print(real)

