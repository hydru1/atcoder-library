def Manacher(S):
    #文字iを中心とする最長の回文の半径を記録した配列をO(|S|)で構築するアルゴリズム
    def main(S,len_S):
        R=[0 for _ in range(len_S)]
        i=0
        j=0
        while(i<len_S):
            while(i-j>=0 and i+j<len_S):
                if S[i-j]==S[i+j]:
                    j+=1
                else:
                    break
            R[i]=j
            k=1
            while(i-k>=0):
                if k+R[i-k]<j:
                    R[i+k]=R[i-k]
                    k+=1
                else:
                    break
            i+=k
            j-=k
        return R

    len_S=len(S)
    if len_S%2==1:
        return main(S,len_S)
    else:
        T=S[0]
        for i in range(1,len_S):
            T+="$"
            T+=S[i]
        R=main(T,2*len_S-1)
        RR=[1]
        for i in range(1,len_S):
            r=R[2*i]
            if r%2==1:
                RR.append(r//2+1)
            else:
                RR.append(r//2)
        return RR
