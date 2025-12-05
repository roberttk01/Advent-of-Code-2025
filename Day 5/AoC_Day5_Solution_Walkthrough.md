# Day 5: Cafeteria

⭐ Part 1 | ⭐ Part 2

---

## Problem Summary

### Part 1
**Story:** The Elves break through a wall and discover a cafeteria. In the kitchen, staff are panicking — their new inventory management system makes it impossible to tell which ingredients are fresh and which are spoiled.

**Task:** Given a database with fresh ingredient ID ranges (inclusive, can overlap) and a list of available ingredient IDs, count how many available IDs are fresh (fall within at least one range).

### Part 2
**Story:** The Elves start hauling spoiled inventory to the trash chute. To stop bothering you in the future, they want to know ALL IDs the ranges consider fresh.

**Task:** Ignore the available ingredient IDs. Count the total number of unique IDs covered by all fresh ranges (handling overlaps).

---

## Approach

### Part 1
I parsed the input into two sections using a flag that flips when hitting the blank line delimiter. For each available ingredient ID, I checked if it fell within any range using simple `start <= id <= end` comparisons. Straightforward range membership checking.

### Part 2
Since ranges can overlap, I couldn't just sum their lengths. I used a merge algorithm: sort ranges by start value, then iterate through — if the current range overlaps the last merged range, extend it; otherwise, append as a new interval. Finally, sum the lengths of all merged intervals. This is essentially what a DIET (Discrete Interval Encoding Tree) does, but simplified for batch processing.

---

## Solution

### Part 1
```python
def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    ranges = []
    ingredient_ids = []
    parsing_ranges = True

    for line in lines:
        line = line.strip()
        if line == "":
            parsing_ranges = False
            continue
        if parsing_ranges:
            ranges.append(tuple(map(int, line.split("-"))))
        else:
            ingredient_ids.append(int(line))

    return ranges, ingredient_ids


def is_fresh(ingredient_id, ranges):
    if not ranges:
        return True
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh(ingredient_ids, ranges):
    count = 0
    for ingredient_id in ingredient_ids:
        if is_fresh(ingredient_id, ranges):
            count += 1
    return count


def main():
    ranges, ingredient_ids = parse_input("input")
    result = count_fresh(ingredient_ids, ranges)
    print(result)


if __name__ == "__main__":
    main()
```

### Part 2
```python
def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    ranges = []
    parsing_ranges = True

    for line in lines:
        line = line.strip()
        if line == "":
            parsing_ranges = False
            continue
        if parsing_ranges:
            ranges.append(tuple(map(int, line.split("-"))))

    return ranges


def merge_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    merged = []

    if not ranges:
        return merged

    merged.append(ranges[0])

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if last_start <= start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


def count_fresh_ids(ranges):
    count = 0
    ranges = merge_ranges(ranges)

    if not ranges:
        return count

    for start, end in ranges:
        count += end - start + 1

    return count


def main():
    ranges = parse_input("input")
    result = count_fresh_ids(ranges)
    print(result)


if __name__ == "__main__":
    main()
```

---

## Key Takeaways
- Blank lines in input can be **section delimiters** — use a flag to track which section you're parsing
- Range merging algorithm: sort by start, then extend or append based on overlap
- DIET (Discrete Interval Encoding Tree) is the generalized data structure for this pattern, but sort-and-merge works great for batch processing

---

## Stats
| Metric | Part 1 | Part 2 |
|--------|--------|--------|
| Time to solve | ~15 min | ~30 min |
| Runtime | Negligible | Negligible |
| Difficulty | Easy | Medium |

---

## Links
- [AoC Day 5](https://adventofcode.com/2025/day/5)
- [Reddit Megathread](https://www.reddit.com/r/adventofcode/search/?q=Day+5+Megathread)
- [GitHub Solution](https://github.com/roberttk01/Advent-of-Code-2025/tree/main/Day%205)
