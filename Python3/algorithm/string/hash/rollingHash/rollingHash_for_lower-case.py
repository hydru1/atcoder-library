class Rolling_Hash():#for lower-case letter
    def __init__(self,S, base=26, mod=2**61-1):
        #type=0: integer sequence , type=1: string         
        
        self.mod=mod
        self.base=base
        self.length=len(S)
        self.power=power=[1]*(len(S)+1)

        L=len(S)
        self.hash=h=[0]*(L+1)

        for i in range(L):
            h[i+1]=(base*h[i]+ord(S[i])-96)%mod
        
        for i in range(L):
            power[i+1]=base*power[i]%mod

    def __hasher(self, X):
        assert len(X)<=len(self)
        h=0
        for i in range(len(X)):
            h=(h*self.base+X[i])%self.mod
        return h

    def get(self, l, r):
        return (self.hash[r]-self.hash[l]*self.power[r-l])%self.mod

    def count(self, T, start=0):
        alpha=self.__hasher(T)

        K=0
        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                K+=1
        return K

    def find(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def rfind(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(len(self)-len(T), start-1, -1):
            if alpha==self[i: i+len(T)]:
                return i
        return -1

    def index(self, T, start=0):
        alpha=self.__hasher(T)

        for i in range(start, len(self)-len(T)+1):
            if alpha==self[i: i+len(T)]:
                return i
        raise ValueError("substring not found")

    def __getitem__(self, index):
        if index.__class__==int:
            if index<0:
                index+=self.length
            assert 0<=index<self.length
            return self.get(index, index+1)
        elif index.__class__==slice:
            assert (index.step==None) or (index.step==1)
            L=index.start if index.start else 0
            R=index.stop if index.stop else len(self)
            if L<0:
                L+=len(self)
            if R<0:
                R+=len(self)
            return self.get(L,R)

    def __len__(self):
        return self.length

    def docking(self, l0, r0, l1, r1):
        """ [l0, r0) と [l1, r1) の部分列をドッキングしたハッシュを返す.
        """

        h0=self.get(l0,r0); h1=self.get(l1,r1)
        return (h0*self.power[r1-l1]+h1)%self.mod

