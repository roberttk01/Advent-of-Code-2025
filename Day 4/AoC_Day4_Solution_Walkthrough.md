# Day 4: Printing Department

⭐ Part 1 | ⭐ Part 2

---

## Problem Summary

### Part 1
**Story:** You're in the North Pole printing department where rolls of paper (`@`) are arranged on a grid. The forklifts are busy moving paper around, but you need them to break through a wall to the cafeteria. To free them up, you need to optimize which rolls they can access.

**Task:** A forklift can access a roll if it has **fewer than 4** rolls of paper in its 8 adjacent positions. Count how many rolls are accessible.

### Part 2
**Story:** The elves want to remove as much paper as possible. Once a roll is accessible, it can be removed — and removing rolls may expose new accessible rolls.

**Task:** Iteratively remove accessible rolls until none remain. Count the **total** rolls removed across all iterations.

---

## Approach

### Part 1
Classic grid neighbor-counting problem. For each cell containing `@`, check all 8 adjacent positions (handling boundary conditions), count how many are also `@`. If the count is less than 4, that roll is accessible. Sum up all accessible rolls.

### Part 2
Extend Part 1 into an iterative simulation. Each round: find all currently accessible rolls, remove them all at once (batch removal is important — removing one-by-one would change neighbor counts mid-scan), then repeat until no accessible rolls remain. The key insight is using a mutable data structure (list of lists instead of list of strings) so we can modify the grid in place.

---

## Solution

### Part 1
```python
"""
Advent of Code 2025 - Day 4, Part 1
Printing Department
"""


def parse_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines


def count_neighbors(grid: list[str], row: int, col: int) -> int:
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '@':
                count += 1
                if i == row and j == col:
                    count -= 1
    return count


def solve(grid: list[str]) -> int:
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                neighbors = count_neighbors(grid, row, col)
                if neighbors < 4:
                    count += 1
    return count


def main():
    grid = parse_input("input")
    result = solve(grid)
    print(f"Part 1: {result}")


if __name__ == "__main__":
    main()
```

### Part 2
```python
"""
Advent of Code 2025 - Day 4, Part 2
Printing Department
"""


def parse_input(filename: str) -> list[list[str]]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        grid = [list(line) for line in lines]
    return grid


def count_neighbors(grid: list[list[str]], row: int, col: int) -> int:
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '@':
                count += 1
                if i == row and j == col:
                    count -= 1
    return count


def find_accessible(grid: list[list[str]]) -> list[tuple[int, int]]:
    neighbors = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                neighbors_count = count_neighbors(grid, row, col)
                if neighbors_count < 4:
                    neighbors.append((row, col))
    return neighbors


def solve(grid: list[list[str]]) -> int:
    count = 0
    while True:
        accessible = find_accessible(grid)
        if not accessible:
            break
        for row, col in accessible:
            grid[row][col] = '.'
        count += len(accessible)
    return count


def main():
    grid = parse_input("input")
    result = solve(grid)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    main()
```

---

## Key Takeaways
- Python's `range(start, end)` is **exclusive** of the end value — `range(row-1, row+2)` gives 3 values, not 2
- `f.readlines()` returns a list; `.strip()` is a string method, not a list method
- Use `list[list[str]]` for mutable grids when you need to modify cells in place (strings are immutable)
- Batch removal matters: find all accessible items first, then remove them all, to avoid changing state mid-iteration

---

## Stats
| Metric | Part 1 | Part 2 |
|--------|--------|--------|
| Time to solve | ~45 min (combined) | |
| Runtime | Negligible | Negligible |
| Difficulty | Easy | Easy-Medium |

---

## Links
- [AoC Day 4](https://adventofcode.com/2025/day/4)
- [Reddit Megathread](https://www.reddit.com/r/adventofcode/comments/1h6jjwp/2025_day_4_solutions/)
- [GitHub Repo](https://github.com/roberttk01/Advent-of-Code-2025)
