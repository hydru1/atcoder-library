from random import random

class SumTree:
    # n=len(A)
    def __init__(self, A):#O(2(n+1))
        self._num_leaves = len(A)
        self._hight = 2
        while(2**(self._hight-1)<self._num_leaves):
            self._hight+=1
        self._x=2**(self._hight-1)-1
        self._tree=[0 for _ in range(self._x+self._num_leaves+1)]
        
        for i in range(self._num_leaves):
            self._tree[i+self._x]=A[i]            
        
        for i in range((len(self._tree)-1)//2,0,-1):
            self._tree[i-1]=self._tree[2*i-1]+self._tree[2*i]
        
    def add(self, index, val):# O(log(n))
        node = 1
        self._tree[0]+=val
        for i in range(self._hight-1):
            if index & 1 << i:
                node = node*2-1
            else:
                node = node*2
            self._tree[node-1]+=val

    def update(self, index, val):# O(log(n))
        self.add(index,val-self._tree[index+self._x])

    def sample(self):# O(log(n))
        p =  random()*self._tree[0]
        node = 1

        for _ in range(self._hight-1):
            if self._tree[2*node-1] >= p:
                node = 2*node
                
            else:
                p -= self._tree[2*node-1]
                node = 2*node+1

        return node-1-self._x