N = int(input())
matrix = [list(map(int,input().split(" "))) for _ in range(N)]
movement = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            shark_row = i
            shark_col = j


def bfs():
    global shark
    global bigger
    global cnt
    global shark_row
    global shark_col
    global q
    global movement
    
    dr = [-1, 0, 0, 1]
    dc = [0, -1, 1, 0]
    
    check=0
    
    while q:
        turns = len(q)
        q.sort()
        for t in range(turns):                                                                   ########checking same depth equally in bfs
    
            r, c = q.pop(0)

            if 0 < matrix[r][c] < shark:                                                         #there is food
                check = 1
                cnt += movement[r][c]-1                                                          #accumulating time
                matrix[r][c] = 0                                                                 #initializing matrix after dine
            
                shark_row, shark_col = r, c                                                      #memorizing coordinate of shark
                bigger += 1                                                                      #counts for growing shark
                if bigger == shark:                                                              #condition for getting bigger
                    shark += 1
                    bigger = 0
                q= []                                                                            
                q.append([shark_row, shark_col])
                movement = [[0]*N for _ in range(N)]
                movement[shark_row][shark_col]=1
                
            for i in range(4):
                nr = r+ dr[i]
                nc = c+ dc[i]
            
                if 0<=nr<N and 0<=nc<N and matrix[nr][nc]<=shark and movement[nr][nc] == 0:      

                    movement[nr][nc] += movement[r][c]+1                                         #counting movements
                    q.append([nr,nc])
                    
            if check == 1:
                check =0
                break
                    
    return cnt

matrix[shark_row][shark_col] = 0
shark = 2
bigger = 0
cnt = 0
q = []
q.append([shark_row,shark_col])
movement[shark_row][shark_col]=1
print(bfs())

