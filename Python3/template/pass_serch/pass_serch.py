from collections import deque

h,w=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(h)]
visit=set()
Q=deque()
ans=0

vy=[1,0]
vx=[0,1]
def pass_serch(y,x):
    global ans
    if A[y][x] in visit:
        return 
    
    if (y,x)==(h-1,w-1):
        ans+=1
        return
    
    visit.add(A[y][x])
    Q.append(A[y][x])
    for k in range(len(vy)):
        ny=y+vy[k]
        nx=x+vx[k]
        if 0<=ny<len(A) and 0<=nx<len(A[0]):
            pass_serch(ny,nx)
            while(True):
                a=Q.pop()
                if a==A[y][x]:
                    Q.append(A[y][x])
                    break
                visit.remove(a)
    Q.pop()
    visit.remove(a)
    
pass_serch(0,0)
print(ans)