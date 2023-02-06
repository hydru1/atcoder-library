class combination():
    def __init__(self,n,mod):
    
        self.mod=mod
        self.fact = [1,1] # x!
        self.factinv = [1,1] # (x!)^(-1)
        inv = [0,1]
        for i in range(2,n+1):
            self.fact.append((self.fact[-1]*i)%mod)
            inv.append((-inv[mod%i]*(mod//i))%mod)
            self.factinv.append((self.factinv[-1]*inv[-1])%mod)

    def cmb(self,n,r):
        r=min(r,n-r)
        return self.fact[n]*self.factinv[r]*self.factinv[n-r]%self.mod

