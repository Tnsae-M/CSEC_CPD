s1,s2,s3,s4=map(int,input().split())
shoes=[s1,s2,s3,s4]
count=0
final=0
for i in range(len(shoes)):
    for j in range(i+1,len(shoes)):
        if shoes[i]==shoes[j]:
            count+=1
            break
if count==4:
    final=count-1
else:
    final=count
print(final)