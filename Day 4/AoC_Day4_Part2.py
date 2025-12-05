"""
Advent of Code 2025 - Day 4, Part 2
Printing Department
"""


def parse_input(filename: str) -> list[list[str]]:
    """
    Parse the puzzle input file.

    Args:
        filename: Path to the input file

    Returns:
        Grid as list of lists (mutable, so we can remove rolls)
    """
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        grid = [list(line) for line in lines]
    return grid


def count_neighbors(grid: list[list[str]], row: int, col: int) -> int:
    """
    Count how many '@' rolls are in the 8 adjacent positions.

    (Same logic as Part 1)

    Args:
        grid: The paper roll grid
        row: Current row position
        col: Current column position

    Returns:
        Number of adjacent '@' symbols
    """
    # TODO: Reuse/adapt Part 1 logic
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '@':
                count += 1
                # Handle boundary conditions
                if i == row and j == col:
                    count -= 1
                    # Don't count the current cell
    return count


def find_accessible(grid: list[list[str]]) -> list[tuple[int, int]]:
    """
    Find all rolls that can currently be accessed (< 4 neighbors).

    Args:
        grid: The paper roll grid

    Returns:
        List of (row, col) positions of accessible rolls
    """
    # TODO: Iterate grid, collect positions where cell is '@' and neighbors < 4
    neighbors = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                neighbors_count = count_neighbors(grid, row, col)
                if neighbors_count < 4:
                    neighbors.append((row, col))
    return neighbors


def solve(grid: list[list[str]]) -> int:
    """
    Count total rolls removed through iterative removal.

    Approach:
        - Loop until no accessible rolls remain:
            1. Find all currently accessible rolls
            2. If none found, break
            3. Remove them from grid (set to '.')
            4. Add count to running total
        - Return total removed

    Args:
        grid: The paper roll grid (will be mutated)

    Returns:
        Total number of rolls removed
    """
    # TODO: Implement iterative removal loop
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
