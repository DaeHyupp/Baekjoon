import sys
sys.setrecursionlimit(1000000)

def dfs(height, width):
    global board, matrix
    if matrix[height][width] != 1 or board[height][width] == 1 : return -1

    board[height][width] = 1
    if height>0:
        if matrix[height-1][width] == 1 and board[height-1][width] != 1: dfs(height-1,width)
        if width>0:
            if matrix[height-1][width-1] == 1 and board[height-1][width-1] != 1 : dfs(height-1,width-1)
        if width<w-1:
            if matrix[height-1][width+1] == 1 and board[height-1][width+1] != 1: dfs(height-1,width+1)
    if height<h-1:
        if matrix[height+1][width] == 1 and board[height+1][width] != 1: dfs(height+1,width)
        if width>0:
            if matrix[height+1][width-1] == 1 and board[height+1][width-1] != 1: dfs(height+1,width-1)
        if width<w-1:
            if matrix[height+1][width+1] == 1 and board[height+1][width+1] != 1: dfs(height+1,width+1)
    if width>0:
        if matrix[height][width-1] == 1 and board[height][width-1] != 1: dfs(height,width-1)
        if height>0:
            if matrix[height-1][width-1] == 1 and board[height-1][width-1] != 1: dfs(height-1,width-1)
        if height<h-1:
            if matrix[height+1][width-1] == 1 and board[height+1][width-1] != 1: dfs(height+1,width-1)
    if width<w-1:
        if matrix[height][width+1] == 1 and board[height][width+1] != 1: dfs(height,width+1)
        if height>0:
            if matrix[height-1][width+1] == 1 and board[height-1][width+1] != 1: dfs(height-1,width+1)
        if height<h-1:
            if matrix[height+1][width+1] == 1 and board[height+1][width+1] != 1: dfs(height+1,width+1)

    
    return 0
    



while 1:
    w, h = map(int, input().split(' '))
    if w==0 and h==0: break
    board = [[0]*(w) for i in range(h)]
    matrix = [[0]*(w) for i in range(h)]
    for i in range(h):
        matrix[i] =  list(map(int,input().split(' ')))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) != -1:
                cnt +=1

    print(cnt)
        

