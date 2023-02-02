from heapq import heappop,heappush

def dijkstra(G,r):
    inf=2**61-1

    v=len(G)
    Q=[(0,r)]
    dist=[inf for _ in range(v)]

    while(Q):
        cost,node=heappop(Q)
        if dist[node]!=inf:
            continue
        dist[node]=cost
        for _node,_cost in G[node]:
            if dist[_node]!=inf:
                continue
            heappush(Q,(_cost+cost,_node))

    return dist
