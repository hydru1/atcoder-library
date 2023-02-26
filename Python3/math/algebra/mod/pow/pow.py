#m**nをpZ/Z上で求める
def pow(m,n,p):
    if n>=0:
        return pow(m,n,p)
    else:
        ie=pow(m,p-2,p)
        return pow(ie,-n,p)
