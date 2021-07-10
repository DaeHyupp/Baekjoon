N = int(input())

for i in range(N):
    q = []
    q.append(1)
    q.append(1)
    num = int(input())
    if num == 0:
        print("1 0")
        continue
    elif num==1:
        print("0 1")
        continue
    for j in range(num-2):
        a= q[1+j]+q[j]
        q.append(a)
    
    print("%d %d" %(q[num-2],q[num-1]))

