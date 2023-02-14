def divisor(n):
    i=1
    result1=[]
    result2=[]
    while(i*i<n):
        if n%i==0:
            result1.append(i)
            result2.append(n//i)
        i+=1
    if i*i==n:
        result1.append(i)
    return result1+result2[::-1]
