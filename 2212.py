import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().rstrip().split(" ")))
ran = []
if N <= K :
    print(0)
else:
    sensor.sort()
    for i in range(N-1):
        ran.append(abs(sensor[i]-sensor[i+1]))
    ran.sort()
    for i in range(K-1):
        ran.pop(-1)
    print(sum(ran))
        

