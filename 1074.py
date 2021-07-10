def sol(n,r,c):
    global cnt

    if n==1:
        if r==0 and c==0 :return cnt
        if r==0 and c==1 :return cnt+1
        if r==1 and c==0 :return cnt+2
        if r==1 and c==1 :return cnt+3
    
    length = 2**n
    
    if r> length/2 -1 :
        r = r -length/2
        cnt += length*(length/2)
    if c > length/2 -1:
        c = c -length/2
        cnt +=(length/2)*(length/2)
    return sol(n-1,r,c)

N, r, c = map(int, input().split(" "))
cnt =0
print(int(sol(N,r,c)))

