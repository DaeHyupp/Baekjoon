import sys
input = sys.stdin.readline

N = int(input())
exams = []
board= [0]*1001
for i in range(N):
    exams.append(list(map(int, input().split(" "))))
exams = sorted(exams,key=lambda x: x[1],reverse=True)
for i in range(N):
    if board[exams[i][0]] == 0:
        board[exams[i][0]] = exams[i][1]
    else:
        for j in range(exams[i][0]-1,0,-1):
            if board[j] == 0:
                board[j] = exams[i][1]
                break
print(sum(board))

