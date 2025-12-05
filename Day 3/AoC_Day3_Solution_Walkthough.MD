# Day 03: Lobby

P Part 1 | P Part 2

---

## Problem Summary

### Part 1

**Story:** You descend into the vast North Pole lobby and pass through security, only to find all the elevators offline  fried by an electrical surge. An Elf suggests taking the escalator down to the printing department, but it needs emergency power. Nearby batteries labeled with joltage ratings (1-9) are arranged in banks.

**Task:** For each bank of batteries, turn on exactly **2 batteries** to form a 2-digit number (first battery = tens digit, second = units digit, maintaining their order). Find the maximum joltage each bank can produce and sum them all.

### Part 2

**Story:** The escalator still won't budge  not enough joltage to overcome static friction. The Elf hits the "joltage limit safety override" button (after many confirmations), and now you need more power.

**Task:** Same as Part 1, but now turn on exactly **12 batteries** per bank to form a 12-digit number. Find the maximum joltage from each bank and sum them.

---

## Approach

### Part 1

I used nested for loops to iterate over all pairs `(i, j)` where `i < j`. For each pair, I concatenated the digits to form a 2-digit number and tracked the maximum. Simple brute force that works fine for choosing 2 from ~15 batteries.

### Part 2

The jump from 2 to 12 batteries broke the brute-force approach  12 nested loops isn't practical. The solution required a **greedy algorithm**: at each step, pick the largest digit that still leaves enough remaining digits to fill the rest of the 12 positions. This builds the maximum number digit-by-digit from left to right.

---

## Solution

### Part 1

```python
def parse_input(filename):
    """Read battery banks from input file."""
    with open(filename, 'r') as f:
        batteries = f.read().strip().split('\n')
    return batteries


def max_joltage(bank):
    """Find the maximum 2-digit joltage from a bank by picking exactly 2 batteries."""
    joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            if int(bank[i]) * 10 + int(bank[j]) > joltage:
                joltage = int(bank[i]) * 10 + int(bank[j])
    return joltage


def main():
    banks = parse_input('input')
    total = sum(max_joltage(bank) for bank in banks)
    print(f"Total output joltage: {total}")


if __name__ == '__main__':
    main()
```

### Part 2

```python
def parse_input(filename):
    """Read battery banks from input file."""
    with open(filename, 'r') as f:
        return f.read().strip().split('\n')


def max_joltage(bank, num_batteries=12):
    """Find the maximum 12-digit joltage using greedy selection."""
    result = ""
    start = 0

    for k in range(num_batteries):
        remaining_needed = num_batteries - k - 1
        end = len(bank) - remaining_needed

        best_digit = '0'
        best_index = start
        for i in range(start, end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i

        result += best_digit
        start = best_index + 1

    return int(result)


def main():
    banks = parse_input('input')
    total = sum(max_joltage(bank) for bank in banks)
    print(f"Total output joltage: {total}")


if __name__ == '__main__':
    main()
```

---

## Key Takeaways

- Brute force works for small selection sizes but doesn't scale
- When maximizing a number digit-by-digit, **greedy selection** is the pattern: pick the largest valid digit at each position
- The "valid window" constraint is key  you can only pick a digit if enough remain to fill the rest
- Character comparison works for single digits: `'9' > '8' > ... > '0'`
- Still learning to recognize when Part 2 requires a fundamentally different approach

---

## Stats

| Metric | Part 1 | Part 2 |
|--------|--------|--------|
| Time to solve | ~30 min | ~10 min |
| Runtime | Negligible | Negligible |
| Difficulty | Easy | Medium |

---

## Links

- [AoC Day 3](https://adventofcode.com/2025/day/3)
- [Reddit Megathread](https://www.reddit.com/r/adventofcode/search/?q=Day+3+Megathread)
- [GitHub Solution](https://github.com/roberttk01/Advent-of-Code-2025/tree/main/Day%203)
