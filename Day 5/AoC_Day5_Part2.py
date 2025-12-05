def parse_input(filename):
    """
    Parse the input file to get fresh ingredient ID ranges.
    Only need the ranges section (before blank line).
    Returns list of (start, end) tuples.
    """
    with open(filename) as f:
        lines = f.readlines()

    ranges = []
    parsing_ranges = True  # START: we're in the ranges section

    for line in lines:
        line = line.strip()
        if line == "":
            parsing_ranges = False  # SWITCH: now we're in IDs section
            continue                # skip the blank line itself
        if parsing_ranges:
            # We're still in the top section → it's a range
            ranges.append(tuple(map(int, line.split("-"))))
        else:
            # We're past the blank line → it's an ingredient ID 
            pass  # TODO
                
    return ranges


def merge_ranges(ranges):
    """
    Merge overlapping/adjacent ranges into non-overlapping intervals.

    Algorithm:
    1. Sort ranges by start value
    2. Initialize merged list with first range
    3. For each subsequent range:
       - If it overlaps or is adjacent to last merged range, extend it
       - Otherwise, append as new interval

    Returns list of merged (start, end) tuples.
    """

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
    """
    Count how many unique ingredient IDs are covered by the ranges.

    Steps:
    1. Merge overlapping ranges
    2. Sum lengths of each merged interval (end - start + 1 for inclusive)
    """
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
