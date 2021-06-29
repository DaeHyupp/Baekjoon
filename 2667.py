N = int(input())
matrix=[]
for i in range(N):
    matrix.append(list(map(int,input())))
visit_mat = [[0]*N for i in range(N)]

def dfs(row, col, count):
    if matrix[row][col] ==1 and visit_mat[row][col] == 0:
        visit_mat[row][col]=1
        count +=1
        if col+1 < N:
            if matrix[row][col+1] ==1 and visit_mat[row][col+1] ==0:
                count = dfs(row, col+1, count)
        if col>0:
            if matrix[row][col-1] ==1 and visit_mat[row][col-1] ==0:
                count = dfs(row, col-1, count)
        if row+1 < N:
            if matrix[row+1][col] ==1 and visit_mat[row+1][col] ==0:
                count = dfs(row+1, col, count)
        if row>0:
            if matrix[row-1][col] ==1 and visit_mat[row-1][col] ==0:
                count = dfs(row-1, col, count)
    return count

answer=[]

for i in range(N):
    for j in range(N):
        count = 0
        num=dfs(i,j,count)
        if num != 0:
            answer.append(num)
length = len(answer)
for i in range(1,length):
    if i==length : break
    for j in range(length-i):
        if answer[j]>answer[j+1]:
            tmp = answer[j]
            answer[j] = answer[j+1]
            answer[j+1] = tmp
print(len(answer))

for i in range(len(answer)):
    print(answer[i])

