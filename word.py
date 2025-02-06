word=list(map(str,input()))
up=0
low=0
for i in range(len(word)):
    if word[i-1].isupper():
        up+=1
    elif word[i-1].islower():
        low+=1
if up>low:
    print(''.join(word).upper())
elif up<low:
    print(''.join(word).lower())
else:
    print(''.join(word).lower())
