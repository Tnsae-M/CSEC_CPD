a1,a2,a3,a4=map(int,input().split())
order=input().strip()
calories=0
for i in order:
    if i=="1":
        calories+=a1
    elif i=="2":
        calories+=a2
    elif i=="3":
        calories+=a3
    else:
        calories+=a4
print(calories)