import sys
sys.setrecursionlimit(10**8)

class LowLinks:
    def __init__(self, G, root=0):
        v=len(G)
        self.G = G
        self.root = root
        self.ord = [None] * v
        self.low = [None] * v
        self.cnt = 0
        self.bridges = []
        self.articulations = set()
        self.par = [None] * v
        self.search(self.root)

    def search(self, x):
        self.ord[x] = self.cnt
        self.low[x] = self.cnt
        self.cnt += 1
        dim = 0
        for to in self.G[x]:
            if to == self.par[x]:continue
            if self.ord[to] != None:
                self.low[x] = min(self.low[x], self.ord[to])
            else:
                self.par[to] = x
                self.search(to)
                dim += 1
                self.low[x] = min(self.low[x], self.low[to])

                if x != self.root and self.ord[x] <= self.low[to]:
                    self.articulations.add(x)

            if x == self.root and dim > 1:
                self.articulations.add(x)

            if self.ord[x] < self.low[to]:
                self.bridges.append((x, to))