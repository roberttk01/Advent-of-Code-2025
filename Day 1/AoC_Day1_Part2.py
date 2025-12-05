from math import floor

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
      count += (start + magnitude[i]) // 100
      start += magnitude[i]
      start = start % 100
    else:
        if start == 0:
            count += magnitude[i] // 100
        elif start > 0 and magnitude[i] >= start:
            count += 1 + (magnitude[i] - start) // 100
        start -= magnitude[i]
        start = start % 100
        
print(count)