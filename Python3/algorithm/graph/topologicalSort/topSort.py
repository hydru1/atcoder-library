from collections import deque
def kahn_topsort(G):
    N=len(G)
    deg=[len(G[i]) for i in range(N)]

    S=deque(i for i in range(N) if deg[i]==0)
    ans=[]

    while S:
        v = S.popleft()
        ans.append(v)
        for t in G[v]:
            deg[t] -= 1
            if deg[t]==0:
                S.append(t)
    if len(ans)!=N:
        return []
    return ans