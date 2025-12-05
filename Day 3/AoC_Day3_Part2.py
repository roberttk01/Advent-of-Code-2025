def parse_input(filename):
    """Read battery banks from input file."""
    with open(filename, 'r') as f:
        return f.read().strip().split('\n')


def max_joltage(bank, num_batteries=12):
    """
    Find the maximum 12-digit joltage from a bank by picking exactly 12 batteries.

    Approach (greedy):
    - To maximize a number, you want the largest digits as early as possible
    - At each position, pick the largest digit that still leaves enough
      remaining digits to fill the rest of the positions

    Example: bank = "234234234234278", need 12 digits
    - Bank has 15 chars, need to pick 12, so skip 3
    - For 1st digit: can pick from indices 0 to 3 (must leave 11 more)
      Find max in that window, note its index, move forward
    - For 2nd digit: can pick from (prev_index + 1) to (new limit)
    - Repeat until 12 digits selected

    Key constraint at step k (0-indexed):
    - You've picked k digits so far
    - Need (num_batteries - k) more digits
    - Current search starts at some index `start`
    - Latest you can pick from: len(bank) - (num_batteries - k)
    """
    result = ""
    start = 0

    for k in range(num_batteries):
        # How many digits still needed after this one?
        remaining_needed = num_batteries - k - 1

        # Latest index we can pick from (must leave `remaining_needed` after it)
        end = len(bank) - remaining_needed

        # Find max digit in window [start, end)
        best_digit = '0'
        best_index = start
        for i in range(start, end):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_index = i

        # Add to result, move start past the picked index
        result += best_digit
        start = best_index + 1

    return int(result)


def main():
    banks = parse_input('input')

    total = 0
    for bank in banks:
        total += max_joltage(bank)

    print(f"Total output joltage: {total}")


if __name__ == '__main__':
    main()
