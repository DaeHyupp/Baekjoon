import sys
input = sys.stdin.readline

N = int(input().rstrip())
lists = list(map(int,list(input().rstrip().split(" "))))
M = int(input().rstrip())
#find = list(map(int,list(input().rstrip().split(" "))))
lists.sort()
#idx = 0
#find_dic = {}
#for findings in sorted(find):
#    cnt = 0
#    if findings not in find_dic:
#        while idx < N:
#            if findings == lists[idx]:
#                cnt +=1
#                idx +=1
#            elif findings > lists[idx]:
#                idx +=1
#            else: break
#        find_dic[findings] = cnt
#
#for findings in find:
#    print(find_dic[findings], end=' ')

def BS(start,end,target):
    if start>end: return 0
    mid = (start+end)//2
    if lists[mid] == target: return lists[start:end+1].count(target)
    elif lists[mid] < target: return BS(mid+1,end,target)
    else: return BS(start,mid-1,target)

find_dic = {}
find = list(map(int,list(input().rstrip().split(" "))))
for findings in find:
    if findings not in find_dic:
        find_dic[findings]=BS(0,N-1,findings)

for findings in find:
    print(find_dic[findings], end=' ')

