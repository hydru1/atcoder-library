class joint_cumlative_sum():
    def __init__(self,A,mod):
        self.mod=mod
        self.S=[[0] for _ in range(mod)]
        for i in range(len(A)):
            self.S[i%mod].append(self.S[i%mod][-1]+A[i])
        
    # [l,r]の範囲でindexがiと合同(mod)な要素の総和
    def joint_sum(self,l,r,i):
        i=i%self.mod
        ind1=(l+i)%self.mod
        ind2f=(l+i)//self.mod
        ind2e=ind2f+(r-l-i)//self.mod+1
        return self.S[ind1][ind2e]-self.S[ind1][ind2f]
    