team_number=int(input())
home_jersey=[]
away_jersey=[]
count=0
for i in range(team_number):
    a,b=map(int,input().split())
    home_jersey.append(a)
    away_jersey.append(b)
for i in home_jersey:
    for j in away_jersey:
        if i==j:
            count+=1
print(count)



