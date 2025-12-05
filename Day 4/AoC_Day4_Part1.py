"""
Advent of Code 2025 - Day 4, Part 1
Printing Department
"""


def parse_input(filename: str) -> list[str]:
    """
    Parse the puzzle input file.

    Args:
        filename: Path to the input file

    Returns:
        List of strings representing the grid rows
    """
    with open(filename, 'r') as f:
        # TODO: Read lines into a list (strip whitespace)
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        return lines


def count_neighbors(grid: list[str], row: int, col: int) -> int:
    """
    Count how many '@' rolls are in the 8 adjacent positions.

    Approach:
        - Check all 8 directions: N, NE, E, SE, S, SW, W, NW
        - Handle boundary conditions (don't go out of bounds)
        - Count occurrences of '@'

    Args:
        grid: The paper roll grid
        row: Current row position
        col: Current column position

    Returns:
        Number of adjacent '@' symbols
    """
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


def solve(grid: list[str]) -> int:
    """
    Count rolls of paper accessible by forklifts.

    Approach:
        - Iterate through each cell in the grid
        - If cell is '@', count its neighbors
        - If neighbor count < 4, this roll is accessible
        - Return total count of accessible rolls

    Args:
        grid: The paper roll grid

    Returns:
        Number of accessible rolls
    """
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
