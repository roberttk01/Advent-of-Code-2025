def parse_input(filename):
    """Read battery banks from input file."""
    with open(filename, 'r') as f:
        batteries = f.read().strip().split('\n')
    
    return batteries    
    

def max_joltage(bank):
    """
    Find the maximum 2-digit joltage from a bank by picking exactly 2 batteries.

    Approach:
    - Pick two positions i < j from the bank string
    - bank[i] becomes tens digit, bank[j] becomes units digit
    - Find the pair that maximizes the resulting 2-digit number
    """
    joltage = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            if i < j and int(bank[i])*10 + int(bank[j]) > joltage:
                joltage = int(bank[i])*10 + int(bank[j])
    return joltage


def main():
    banks = parse_input('input')

    total = 0
    for bank in banks:
        total += max_joltage(bank)

    print(f"Total output joltage: {total}")


if __name__ == '__main__':
    main()
