def sub(s):
    n=len(s)
    sl=[]
    for l in range(1,n+1):
        for i in range(n-l+1):
            ss=s[i:i+l]
            sl.append(ss)
    return sl
s="ADOBECODEBANC"
print(sub(s))