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
    # Pattern must repeat at least twice, so max pattern length is length//2
    for pattern_len in range(1, length // 2 + 1):
        # Length must be divisible by pattern length
        if length % pattern_len != 0:
            continue

        pattern = s[:pattern_len]
        repetitions = length // pattern_len

        # Check if pattern repeated gives us the original string
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
