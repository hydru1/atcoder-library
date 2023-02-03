def MP(S):
    #文字列S[0,i-1]の接頭辞と接尾辞が最大何文字一致しているか」を記録した配列をO(|S|)で構築するアルゴリズム
    len_S=len(S)
    A=[-1]
    j=-1
    for i in range(len_S):
        while(j>=0 and S[i]!=S[j]):
            j=A[j]
        j+=1
        A.append(j)
    return A
format