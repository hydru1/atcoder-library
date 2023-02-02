from heapq import heappush, heappop

def chu_liu_edmonds(G,r):    
    def f(v,edges,r):
        if v <= 1:
            return 0
        q = [[] for _ in range(v)]
        for s, t, w in edges:
            heappush(q[t], (w, s))
        M = [(0, -1) for _ in range(v)]
        for t in range(v):
            if t != r:
                w, s = heappop(q[t])
                M[t] = (w, s)
        
        used = [False for _ in range(v)]
        hist = []
        cycle = []
        for t in range(v):
            w, s = M[t]
            if s == -1 or used[t] == True:
                continue
            if used[t] == False:
                used[t] = True
                hist += [t]
                tt = s
                while used[tt] == False:
                    used[tt] = True
                    hist += [tt]
                    w, s = M[tt]
                    if s == -1:
                        hist = []
                        break
                    tt = s
                if used[tt] == True and s != -1 and 0 < len(hist):
                    try:
                        k = hist.index(tt)
                        cycle = hist[k:]
                    except:
                        continue
                    finally:
                        pass
                    break
                    
        if len(cycle) == 0:
            return sum(m[0] for m in M)

        parent = min(cycle)
        rn = [0 for _ in range(v)]
        k = 0
        for t in range(v):
            if k == parent:
                k += 1
            if t in cycle:
                rn[t] = parent
            else:
                rn[t] = k
                k += 1
                
        Vp = v - len(cycle) + 1
        Ep = []
        for s, t, w in edges:
            if s in cycle:
                if t in cycle:
                    continue
                else:
                    Ep += [[parent, rn[t], w]]
            else:
                if t in cycle:
                    Ep += [[rn[s], parent, w - M[t][0]]]
                else:
                    Ep += [[rn[s], rn[t], w]]
        r = rn[r]
        return f(Vp, Ep, r) + sum(M[t][0] for t in cycle)

    v=len(G)
    edges=[]
    for i in range(v):
        for j,c in G[i]:
            edges.append((i,j,c))
    return f(v,edges,r)

v,e,r=map(int,input().split())
G=[[] for _ in range(v)]
for _ in range(e):
    a,b,c=map(int,input().split())
    G[a].append((b,c))

print(chu_liu_edmonds(G,r))
