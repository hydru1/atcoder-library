from collections import deque

def bfs(G,r):
    n=len(G)
    Q=deque()
    Q.append(r)
    inf=2**61-1
    dist=[inf for _ in range(n)]
    dist[r]=0
    while(Q):
        s=Q.popleft()
        for t in G[s]:
            if dist[t]==inf:
                dist[t]=dist[s]+1
                Q.append(t)
    
    return dist