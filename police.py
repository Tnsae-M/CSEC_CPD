num_events=int(input())
events=list(map(int,input().split()))
crime,police=0,0
for event in events:
    if event == -1:
        if police > 0:
            police -= 1
        else:
            crime += 1
    else:
        police += event
print(crime)





    

