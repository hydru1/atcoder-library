import sys
sys.setrecursionlimit(10**8)

def LowLinks(G, root=0):
 
    v=len(G)

    ord = [None] * v
    low = [None] * v
    bridges = []
    articulations = set()
    par = [None] * v


    def search(x,cnt):
        ord[x] = cnt
        low[x] = cnt
        cnt += 1
        dim = 0
        for to in G[x]:
            if to == par[x]:continue
            if ord[to] != None:
                low[x] = min(low[x], ord[to])
            else:
                par[to] = x
                search(to,cnt)
                dim += 1
                low[x] = min(low[x], low[to])

                if x != root and ord[x] <= low[to]:
                    articulations.add(x)

            if x == root and dim > 1:
                articulations.add(x)

            if ord[x] < low[to]:
                bridges.append((x, to))
    
    search(root,0)

    return bridges