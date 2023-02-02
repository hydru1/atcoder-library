from collections import deque

def bellman_ford(G,r):
    inf=2**61-1

    n=len(G)
    dist = [inf for _ in range(n)] 
    dist[r]=0 

    for i in range(n):
        update = False
        visit=[0 for _ in range(n)]
        Q=deque([r])
        while(Q):
            s=Q.pop()
            for t,c in G[s]:
                if dist[t] > dist[s] + c:
                    dist[t] = dist[s] + c
                    update = True
                if visit[t]==0:
                    visit[t]=1
                    Q.append(t)

        if update==False:
            break

        if i==n-1 and update==True:
            return -1 #exist negative cycle
    return dist