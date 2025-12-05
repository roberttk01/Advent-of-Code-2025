def parse_input(filename):
    """
    Parse the input file into two parts:
    1. List of ranges as (start, end) tuples
    2. List of ingredient IDs to check

    Split on blank line. Ranges are "X-Y" format.
    """
    with open(filename) as f:
        lines = f.readlines()

    ranges = []
    ingredient_ids = []
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
            ingredient_ids.append(int(line))
                
    return ranges, ingredient_ids


def is_fresh(ingredient_id, ranges):
    """
    Check if an ingredient ID falls within ANY of the given ranges.
    Ranges are inclusive on both ends.
    """
    if not ranges:
        return True
    for start, end in ranges:
        if start <= ingredient_id <= end:
            return True
    return False


def count_fresh(ingredient_ids, ranges):
    """
    Count how many ingredient IDs are fresh.
    """
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
