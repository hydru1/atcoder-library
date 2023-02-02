def warshall_floyd(G):
    inf=2**61-1
    v=len(G)

    dist=[[inf for _ in range(v)] for _ in range(v)]
    
    for i in range(v):
        dist[i][i]=0

        for node,cost in G[i]:
            dist[i][node]=cost

    for k in range(v):
        for i in range(v):
            if dist[i][k]==inf:
                continue
            for j in range(v):
                if dist[k][j]==inf:
                    continue
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
        
    for i in range(v):
        if dist[i][i]!=0:
            return -1

    return dist