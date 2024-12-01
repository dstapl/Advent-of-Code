# Performing `python solution.py < input.txt`
FILE = open(0).readlines()

# Advent of Code day 4 2023 part 1
# Example input inside test.txt

# For each card: Check how many numbers on the left, match the numbers on the right
# 1 point for first match, double the points for subsequent matches
# Sum total points for each card as return value
# Example `card`: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

def part1():
    # Total points for each card
    total = 0

    for card in FILE:
        # Remove the "Card X: " part, variable length since X could be any integer
        card = card[card.find(':') + 2:]
        # Split the card into two parts, left and right
        left, right = map(str.split, card.split('|'))   

        # Work out number of matches in the left and right lists
        matches = len(set(left).intersection(right))
        if matches == 0:
            continue
        points = 1 << matches-1
        total += points
    # Print the total
    print(total)


def part2():
    # Key of card number, number of copies of cards
    # Initialize the scratchcards dictionary with all the cards set to 1
    # Upper limit from number of lines in input file
    n_lines = len(FILE)
    scratchcards = dict.fromkeys(range(0, n_lines), 1)

    # For each card: Check how many numbers match
    # Add n card copies for the first <number of matches> cards after the current card
    # Where n is the number of copies of the current card

    # Repeat for all cards
    # Return number of cards after all iterations

    # For each card
    for i in range(n_lines):
        # Remove the "Card X: " part, variable length since X could be any integer
        card = FILE[i][FILE[i].find(':') + 2:]
        
        # Split the card into two parts, left and right
        # Split each part into a list of integers
        left, right = map(str.split, card.split('|'))   
        
        # Work out number of matches in the left and right lists
        matches = len(set(left).intersection(right))

        if matches == 0:
            continue

        # Get the number of copies of the current card
        n_copies = scratchcards[i]

        for n in range(1,matches+1):
            # Add n card copies for the first <number of matches> cards after the current card
            scratchcards[i+n] += n_copies

    # Print the total
    print(sum(scratchcards.values()))

if __name__ == '__main__':
    # part1()
    part2()
