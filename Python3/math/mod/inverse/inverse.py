#n**-1をpZ/Z上で求める

#pは素数
def mod_inverse(n,p):
    return pow(n,p-2,p)
