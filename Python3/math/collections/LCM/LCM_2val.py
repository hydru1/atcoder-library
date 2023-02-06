def LCM_2val(a,b):
    def GCD_2val(a,b):
        x=max(a,b)
        y=min(a,b)
        while(y!=0):
            x,y=y,x-(x//y)*y
        return x

    x=a*b//GCD_2val(a,b)
    return x
