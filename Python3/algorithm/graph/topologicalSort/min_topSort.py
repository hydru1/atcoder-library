import heapq
def kahn_min_topsort(G,V,deg):
    S=[v for v in range(V) if deg[v]==0]
    heapq.heapify(S)
    ans=[]
    while(S):
        v=heapq.heappop(S)
        ans.append(v)
        for t in G[v]:
            deg[t]-=1
            if deg[t]==0:
                heapq.heappush(S,t)
    if len(ans)!=V:
        return []
    return ans