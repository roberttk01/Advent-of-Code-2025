# Day 02: Gift Shop

⭐ Part 1 | ⭐ Part 2

---

## Problem Summary

### Part 1

**Story:** After arriving at the North Pole via elevator, you find yourself in the gift shop. A clerk recognizes you and asks for help — a young Elf was playing on the gift shop computer and added a bunch of invalid product IDs to the database. You're given ranges of product IDs to check.

**Task:** Find all "invalid" IDs within the given ranges. An ID is invalid if it consists of a sequence of digits repeated exactly twice (e.g., `55`, `6464`, `123123`). Sum all invalid IDs found.

### Part 2

**Story:** The clerk discovers there are still invalid IDs lurking in the database. Turns out the young Elf was doing other silly patterns too — not just doubled sequences.

**Task:** Now an ID is invalid if it consists of a sequence repeated *at least* twice (2×, 3×, 4×, etc.). For example, `123123123` (123 × 3) and `1111111` (1 × 7) are now invalid. Sum all invalid IDs with these new rules.

---

## Approach

### Part 1

Parse the input into ranges, iterate through each number, and check if it's a "doubled" pattern. A number is invalid if it has even length and the first half equals the second half. Simple string slicing does the job.

### Part 2

Generalize the check to look for *any* repeating pattern. For each number, try all possible pattern lengths from 1 to `len//2`. If the string equals the pattern repeated `len/pattern_len` times, it's invalid.

---

## Solution

### Part 1

```python
def parse_input(filename):
    """Parse the input file into a list of (start, end) tuples."""
    with open(filename, 'r') as f:
        line = f.read().strip()

    ranges = []
    for part in line.split(','):
        start, end = part.split('-')
        ranges.append((int(start), int(end)))

    return ranges


def is_invalid_id(n):
    """Check if a number is 'invalid' (a sequence repeated twice)."""
    s = str(n)

    # Must have even length to be two identical halves
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs within a range."""
    invalid_ids = []

    for n in range(start, end + 1):
        if is_invalid_id(n):
            invalid_ids.append(n)

    return invalid_ids


def main():
    ranges = parse_input('input')

    total = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        total += sum(invalid_ids)

    print(f"Sum of all invalid IDs: {total}")


if __name__ == '__main__':
    main()
```

### Part 2

```python
def parse_input(filename):
    """Parse the input file into a list of (start, end) tuples."""
    with open(filename, 'r') as f:
        line = f.read().strip()

    ranges = []
    for part in line.split(','):
        start, end = part.split('-')
        ranges.append((int(start), int(end)))

    return ranges


def is_invalid_id(n):
    """Check if a number is 'invalid' (a sequence repeated at least twice)."""
    s = str(n)
    length = len(s)

    # Try all possible pattern lengths (1 to length//2)
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue

        pattern = s[:pattern_len]
        repetitions = length // pattern_len

        if pattern * repetitions == s:
            return True

    return False


def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs within a range."""
    invalid_ids = []

    for n in range(start, end + 1):
        if is_invalid_id(n):
            invalid_ids.append(n)

    return invalid_ids


def main():
    ranges = parse_input('input')

    total = 0
    for start, end in ranges:
        invalid_ids = find_invalid_ids_in_range(start, end)
        total += sum(invalid_ids)

    print(f"Sum of all invalid IDs: {total}")


if __name__ == '__main__':
    main()
```

---

## Key Takeaways

- String repetition checks are clean in Python: `pattern * n == s`
- When checking for repeating patterns, iterate over divisors of the string length
- Let Claude cook

---

## Stats

| Metric | Part 1 | Part 2 |
|--------|--------|--------|
| Time to solve | ~5 seconds | ~5 seconds |
| Runtime | Negligible | Negligible |
| Difficulty | Easy | Easy |

---

## Links

- [AoC Day 2](https://adventofcode.com/2025/day/2)
- [Reddit Megathread](https://www.reddit.com/r/adventofcode/search/?q=Day+2+Megathread)
- [GitHub Solution](https://github.com/roberttk01/Advent-of-Code-2025/tree/main/Day%202)
