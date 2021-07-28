import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    min_num = [0,0,1,7,4,2,6,8,10,18,22]
    N = int(input())
    if N >= 11:
        min_numbers = [8 for i in range((N+6)//7)]
        if N%7==1: min_numbers[0]=1;min_numbers[1]=0
        if N%7==2: min_numbers[0]=1
        if N%7==3: min_numbers[0]=2;min_numbers[1]=0;min_numbers[2]=0
        if N%7==4: min_numbers[0]=2;min_numbers[1]=0
        if N%7==5: min_numbers[0]=2
        if N%7==6: min_numbers[0]=6
    
    if N <11:
        print(min_num[N],end=' ')
    else:
        print(min_numbers,sep='',end=' ')
    
    if N%2 !=0:
        max_ans=7
        N = N-3
    else:
        max_ans=1
        N = N-2
    tens=1
    for i in range(N//2):
        max_ans = max_ans*10 + 1
        
    print(max_ans)
    

