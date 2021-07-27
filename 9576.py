import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stu = []
    cnt = 0
    N, M = map(int, input().split(" "))
    board = [0]*(N+1)
    for i in range(M):
        stu.append(list(map(int, input().split(" "))))
    stu = sorted(stu,key=lambda x: x[0])
    stu = sorted(stu,key=lambda x: x[1])
    while stu:
        border1, border2 = stu.pop(0)
        for i in range(border1,border2+1):
            if board[i]==0:
                board[i] = 1
                cnt += 1
                break
    print(cnt)

