A=[[0]]

vy=[1,0,-1,0]
vx=[0,1,0,-1]

for y in range(len(A)):
    for x in range(len(A[0])):
            
            for k in range(4):
                ny=y+vy[k]
                nx=x+vx[k]
                if 0<=ny<len(A) and 0<=nx<len(A[0]):
                    pass