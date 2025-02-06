n=int(input())
stones=input()
count=0
for i in range(n-1):
    if stones[i]==stones[i+1]:
        count+=1
    else:
        count+=0
print(count)