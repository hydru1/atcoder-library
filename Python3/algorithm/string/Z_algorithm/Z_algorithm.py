def Z_algorithm(S):
    #文字列が与えられた時、各 i について「S と S[i:|S|-1] の最長共通接頭辞の長さ」を記録した配列をO(|S|)で構築するアルゴリズム
    len_S=len(S)
    A=[0 for _ in range(len_S)]
    A[0]=len_S
    i=1
    j=0
    while(i<len_S):
        while(i+j<len_S):
            if S[j]==S[i+j]:
                j+=1
            else:
                break
        A[i]=j
        if j==0:
            i+=1
            continue
        k=1
        while(i+k<len_S):
            if k+A[k]<j:
                A[i+k]=A[k]
                k+=1
            else:
                break
        i+=k
        j-=k
    
    return A