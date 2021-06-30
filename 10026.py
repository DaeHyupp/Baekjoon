import sys
sys.setrecursionlimit(1000000)
N = int(input())

matrix1=[]

for i in range(N):
    matrix1.append(list(input()))

check1 = [[0]*N for i in range(N)]

def dfs1(row, col, key, count):
    global area
    area = 1
    check1[row][col] = 1
    if row>0:
        if matrix1[row-1][col]==key and check1[row-1][col] != 1: area = dfs1(row-1, col, key, count)
    if row<N-1:
        if matrix1[row+1][col]==key and check1[row+1][col] != 1: area = dfs1(row+1, col, key, count)
    if col>0:
        if matrix1[row][col-1]==key and check1[row][col-1] != 1: area = dfs1(row, col-1, key, count)
    if col<N-1:
        if matrix1[row][col+1]==key and check1[row][col+1] != 1: area = dfs1(row, col+1, key, count)

    return area

answer1 = 0
answer2 = 0
for i in range(N):
    for j in range(N):
        if check1[i][j] != 1 :
            area = 0
            answer1 += dfs1(i,j,matrix1[i][j], 0)

for i in range(N):
    for j in range(N):
        if matrix1[i][j] == 'G':
            matrix1[i][j] = 'R'


check1 = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        if check1[i][j] != 1: 
            area = 0
            answer2 += dfs1(i,j,matrix1[i][j],0)

print(answer1, answer2)    

