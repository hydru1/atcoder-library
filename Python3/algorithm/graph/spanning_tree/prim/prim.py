from heapq import heappush,heappop

def Prim(G):
    n=len(G)
    visit = [0 for _ in range(n)]

    visit_cnt = 0
    visit[0] = 1
    visit_cnt += 1

    q = []

    for j, c in G[0]:
        heappush(q,(c,j,0))

    edge=[]

    while visit_cnt < n:
        c,i,j = heappop(q)

        if visit[i]:
            continue

        visit[i] = 1
        visit_cnt += 1

        edge.append((i,j)) 

        for j, c in G[i]:
            if visit[j]:
                continue

            heappush(q, (c,j,i))

    return edge
