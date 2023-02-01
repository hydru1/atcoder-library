from collections import deque

mod=10**9+7

n=int(input())
G=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)

fact=[1 for _ in range(n+1)]
inv=[1 for _ in range(n+1)]
factinv=[1 for _ in range(n+1)]
for i in range(2,n+1):
    fact[i]=(fact[i-1]*i)%mod
    inv[i]=(-inv[mod%i]*(mod//i))%mod
    factinv[i]=(factinv[i-1]*inv[i])%mod

def cmb(A):
    S=sum(A)
    ans=fact[S]
    for i in A: 
        ans*=factinv[i] 
        ans%=mod
    return ans

def f(root):
    deg=[len(G[i]) for i in range(n)]
    Q=deque([i for i in range(n) if deg[i]==1])
    DP=[0 for _ in range(n)]
    subtree_size=[1 for _ in range(n)]

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

