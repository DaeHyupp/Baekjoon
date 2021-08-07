import sys
input = sys.stdin.readline

N = int(input())

def solve(n):
    if n==0: return 0
    elif n==1: return 1
    elif n%2: return 1-solve(n//2)
    else: return solve(n//2)

print(solve(N-1))

