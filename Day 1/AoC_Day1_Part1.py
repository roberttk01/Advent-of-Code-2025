raw_rots = open("input").readlines()
direction = []
magnitude = []

for rot in raw_rots:
    direction.append(rot[0])
    magnitude.append(int(rot[1:]))

start = 50
count = 0

for i in range(len(direction)):
    if direction[i] == "R":
        start += magnitude[i]
        start = start % 100
        if start == 0:
            count += 1
    else:
        start -= magnitude[i]
        start = start % 100
        if start == 0:
            count += 1
        
print(count)