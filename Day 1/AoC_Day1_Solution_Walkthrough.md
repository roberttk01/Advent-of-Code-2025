# Day 01: Secret Entrance

⭐ Part 1 | ⭐ Part 2

---

## Problem Summary

### Part 1

**Story:** The Elves have discovered project management and realized they have an emergency — none of them have time to decorate the North Pole! They need you to finish decorating by December 12th. You arrive at the secret entrance, but the password has been changed. A document explains that the password is locked in a safe, with combination instructions attached. However, your recent "North Pole secret entrance security training seminar" taught you that the safe is actually a decoy — the real password is the number of times the dial lands on 0 after any rotation.

**Task:** Simulate a dial numbered 0-99 starting at position 50. Process a sequence of L (left/subtract) and R (right/add) rotations, and count how many times the dial lands exactly on 0 after a rotation completes.

### Part 2

**Story:** The password didn't work. While building a snowman and rolling snowballs, you find another security document in the snow: "Due to newer security protocols, please use password method 0x434C49434B until further notice." From your training, you remember this means counting every *click* that points at 0, not just final positions.

**Task:** Instead of only counting final positions, count *every individual click* that causes the dial to point at 0 — including passes through 0 during a rotation. A single large rotation could cross 0 multiple times.

---

## Approach

### Part 1

I parsed each rotation into a direction and magnitude, then simulated the dial position using modular arithmetic (`% 100`) to handle wraparound. After each rotation, I checked if the position was 0 and incremented the counter.

### Part 2

Instead of simulating every click, I used integer division (`//`) to calculate how many times the dial crosses 0 during each rotation. For right rotations, `(start + magnitude) // 100` gives the crossing count directly. Left rotations required handling edge cases — whether we start at 0, and whether the magnitude is large enough to cross 0 at all.

---

## Solution

### Part 1

```python
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
```

### Part 2

```python
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
```

---

## Key Takeaways

- **Integer division (`//`)** counts how many times you cross a boundary; **modulus (`%`)** tells you where you land after wrapping — they're complementary tools
- Part 2's "count every click" twist is a reminder to think mathematically rather than brute-forcing simulations
- Edge cases in left vs. right movement (starting at 0, crossing through 0) require careful handling to avoid double-counting
- This puzzle is good review material for fundamental operator behavior

---

## Stats

| Metric | Part 1 | Part 2 |
|--------|--------|--------|
| Time to solve | ~60-90 min (combined) | — |
| Runtime | Instant | Instant |
| Difficulty | Easy | Easy |

---

## Links

- [AoC Day 1](https://adventofcode.com/2025/day/1)
- [Reddit Megathread](https://www.reddit.com/r/adventofcode/search/?q=Day+1+Megathread)
- [GitHub Solution](https://github.com/roberttk01/Advent-of-Code-2025/tree/main/Day%201)
