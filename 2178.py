R, C = map(int, input().split(" "))
matrix = [list(map(int,list(input()))) for _ in range(R)]
path = [[0]*C for _ in range(R)]

def bfs():
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    while q:
        
        r, c  = q.pop(0)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0<=nr< R and 0<=nc<C and matrix[nr][nc] == 1 and path[nr][nc] ==0:
                q.append([nr,nc])
                path[nr][nc] += path[r][c]+1
                if nr == R-1 and nc ==C-1:
                    return path[nr][nc]
    return 0

q = []
q.append([0,0])
path[0][0] = 1
print(bfs())
