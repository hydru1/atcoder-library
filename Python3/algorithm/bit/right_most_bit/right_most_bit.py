def Right_Most_Bit(n):
    # 立っている最右端ビット
    x=n-1
    y=x^n
    return y & n