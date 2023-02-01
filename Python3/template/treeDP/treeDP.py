from collections import deque

mod=10**9+7

n=int(input())
G=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)

def f(root):
    deg=[len(G[i]) for i in range(n)]
    Q=deque([i for i in range(n) if deg[i]==1])
    DP=[0 for _ in range(n)]

    def merge(s,A):
        pass

    while(Q):
        s=Q.pop()
        if s==root:
            continue
        
        merge_list=[]
        for t in G[s]:
            if t==root:
                continue
            if deg[t]!=1:
                deg[t]-=1
                if deg[t]==1:
                    Q.append(t)
                continue
            merge_list.append(t)
        
        merge(s,merge_list)

    merge(root,G[root])

    return DP[root]

