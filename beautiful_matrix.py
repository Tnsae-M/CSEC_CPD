mtx=[]
for i in range(5):
    row=list(map(int,input().split()))
    mtx.append(row)
for i in range(5):
    for j in range(5):
        if mtx[i][j]==1:
            print(abs(i-2)+abs(j-2))
            break

