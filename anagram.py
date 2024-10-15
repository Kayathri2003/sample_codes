def anagram(str):
    l=str.split(" ")
    d={}
    for i in l:
        if len(i)>1:
            s="".join(sorted(i))
            
            if s in d:
                d[s]+=1
            else:
                d[s]=1
    su=0   
    for c in d.values():
        if c>1:
            su+=1
    print(su)
anagram("a c bb bb c run unr nur")
    