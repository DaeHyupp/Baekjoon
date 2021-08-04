import sys, itertools
input =sys.stdin.readline

N = int(input())
A = list(map(int,input().rstrip().split(" ")))
iterable_list =[]
a=0
for i in list(map(int,input().rstrip().split(" "))):
    for _ in range(i):
        iterable_list.append(str(a))
    a+=1
combs = set(list(map(''.join, itertools.permutations(iterable_list))))
ans1 = -10**9
ans2 = 10**9

def check():
    global ans1, ans2
    for comb in combs:
        board=[0]*len(A)
        for t in range(len(A)):
            board[t] = A[t]
        tmp=list(map(int,list(comb)))
        
        for i,t in enumerate(tmp):
            if t==0: board[i+1]=board[i]+board[i+1]
            elif t ==1:board[i+1]=board[i]-board[i+1]
            elif t ==2: board[i+1]=board[i]*board[i+1]
            else:
                if board[i]<0: board[i+1]=-(-board[i] // board[i+1])
                else: board[i+1] = board[i]//board[i+1]
        
        ans1 = max(ans1,board[len(A)-1])
        ans2 = min(ans2,board[len(A)-1])

check()
print(ans1)
print(ans2)

