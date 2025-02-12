s=input().upper()
t=input().upper()
s1=list(s)
s2=list(t)
count=0
i=0
for a in range(len(s2)): 
    if s1[i]==s2[a]:
        count+=1
        i+=1
print(count+1)


