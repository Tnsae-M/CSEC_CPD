num_fr,hei_fen=map(int,input().split())
fr_hei=list(map(int,input().split()))
count=0 
for i in fr_hei:
    if i>hei_fen:
        count+=2
    else:
        count+=1
print(count)