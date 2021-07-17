import sys
input = sys.stdin.readline

N = int(input().rstrip())
alkaline = []
acid = []
for i in list(map(int,input().rstrip().split(" "))):
    if i<0: alkaline.append(abs(i))
    else: acid.append(i)
alkaline.sort()
acid.sort()

ans = []
minimum = 2*(10**9)+1
def BS1(start,end,target):

    while start<end:
        mid = (start+end)//2
        if mid == start:
            if abs(acid[start]-target) >= abs(acid[start+1]-target):
                return -target,acid[start+1]
            else: return -target, acid[start]
        if acid[mid] == target: return -target, acid[mid]
        elif acid[mid] < target: start = mid
        else: end = mid
    return -target, acid[start]

def BS2(start,end,target):

    while start<end:
        mid = (start+end)//2
        if mid == start:
            if abs(alkaline[start]-target) >= abs(alkaline[start+1]-target):
                return -alkaline[start+1], target
            else:
                return -alkaline[start], target
            
        if alkaline[mid] == target: return -alkaline[mid], target
        elif alkaline[mid] < target:
            start = mid
        else: end = mid
    return -alkaline[start], target

if len(alkaline) < len(acid):
    for i in alkaline:
        ak, ac = BS1(0,len(acid)-1,i)
        if minimum > abs(ak+ac):
            minimum = abs(ak+ac)
            ans = [ak,ac]
else:
    for i in acid:
        ak, ac = BS2(0,len(alkaline)-1,i)
        if minimum > abs(ak+ac):
            minimum = abs(ak+ac)
            ans = [ak,ac]

if len(acid)>=2:
    if minimum > acid[0]+acid[1]:
        minimum = acid[0]+acid[1]
        ans = [acid[0],acid[1]]

if len(alkaline)>=2:
    if minimum > alkaline[0]+alkaline[1]:
        minimum = alkaline[0]+alkaline[1]
        ans = [-alkaline[1],-alkaline[0]]

print("%d %d" %(ans[0], ans[1]))

