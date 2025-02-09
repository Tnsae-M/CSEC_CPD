import string
item=input().lower()
current='a'
rotation=0
for char in item:
    clockwise_distance=abs(ord(char)-ord(current))
    counter_clockwise=26-clockwise_distance
    rotation+=min(clockwise_distance,counter_clockwise)
    current=char
print(rotation)
