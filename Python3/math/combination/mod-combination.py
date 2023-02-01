mod = 10**9+7
N = int(input())

fact = [1,1] # n!
factinv = [1,1] # (n!)^(-1)
inv = [0,1]#
for i in range(2,N+1):
    fact.append((fact[-1]*i)%mod )
    inv.append((-inv[mod%i]*(mod//i))%mod)
    factinv.append((factinv[-1]*inv[-1])%mod)

def cmb(n,r,mod):
    r = min(r,n-r)
    return fact[n]*factinv[r]*factinv[n-r]%mod


