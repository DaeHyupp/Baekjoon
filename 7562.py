N = int(input())

def bfs():
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]
    while len(q) != 0:
                    
        r, c =q.pop(0)
        for i in range(8):
            nr = r +dr[i]
            nc = c +dc[i]
            if 0<= nr < m and 0<=nc<m and bfsboard[nr][nc] == 0:
                
                bfsboard[nr][nc] += bfsboard[r][c]+1
                if nr == dest_row and nc == dest_col:
                    return bfsboard[r][c]
                
                q.append([nr, nc])
        
    return 0
            
for _ in range(N):
    m = int(input())
    bfsboard = [[0]*m for i in range(m)]
    row, col = map(int, input().split(" "))
    dest_row, dest_col = map(int, input().split(" "))
    bfsboard[row][col] = 1

    q = []
    q.append([row,col])

    print(bfs())

