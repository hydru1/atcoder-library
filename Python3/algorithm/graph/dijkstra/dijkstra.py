from heapq import heapify,heappop,heappush

def dijkstra(G,r):
    v=len(G)
    inf=2**61-1

    Q=[(0,r)]
    heapify(Q)
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
