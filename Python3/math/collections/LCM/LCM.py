def LCM(A):
    def GCD_2val(a,b):
        x=max(a,b)
        y=min(a,b)
        while(y!=0):
            x,y=y,x-(x//y)*y
        return x

    n=len(A)
    x=A[0]
    for i in range(1,n):
        x*=A[i]//GCD_2val(x,A[i])
    return x
