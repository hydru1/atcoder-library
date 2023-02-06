def mod_to_num(D):#D:[(quotient,remainder)]
    def ext_euclid(a, b):
        xs = (a,1,0)
        ys = (b,0,1)
        while ys[0] != 0:
            q = xs[0]//ys[0]
            r = xs[0]%ys[0]
            xs, ys = ys, (r, xs[1]-q*ys[1],xs[2]-q*ys[2])
        return xs

    Q,R=1,0
    for q,r in D:
        g,x,y=ext_euclid(Q,q)
        Q,R=Q*q//g,R*q*y//g+r*Q*x//g
        R%=Q

    return R,Q