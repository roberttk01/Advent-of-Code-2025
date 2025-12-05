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
