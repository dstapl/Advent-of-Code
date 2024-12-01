# Each line is in the form: <hand: str> <value: int>
file = open(0).readlines()

# Coding Camel Cards (Alternative poker)
# Convert file into list of tuples
cards = []
for line in file:
    hand, value = line.split()
    cards.append((hand, int(value)))

# Sort cards by strength of hand
# Hand is always 5 cards long
# From strongest to weakest:
# 1. Five of a kind, where all five cards have the same label: AAAAA
# 2. Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# 3. Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# 4. Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# 5. Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# 6.One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# 7.High card, where all cards' labels are distinct: 23456
# Card labels from strongest to weakest: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
label_strength = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}


def hand_rank(hand):
    # Five of a kind
    unique = set(hand)
    if len(unique) == 1:
        return 7
    
    if len(unique) == 2:
        for card in unique:
            # Full house
            if hand.count(card) == 3:
                return 6
            # Four of a kind
            if hand.count(card) == 4:
                return 5
    if len(unique) == 3:
        for card in unique:
            # Three of a kind
            if hand.count(card) == 3:
                return 4
            # Two pair
            if hand.count(card) == 2:
                return 3
    # One pair
    if len(unique) == 4:
        return 2
    return 1 # High card

# Define sorting function:
# 1. Sort by strength of hand
# 2. If two cards have the same strength, sort by whichever has the highest card label first
# Examples:
# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

# Rank is ordered from weakest to strongest.

def sort_hands(hand1, hand2):
    # Sort by rank of hand
    if hand_rank(hand1) < hand_rank(hand2):
        return -1
    if hand_rank(hand1) > hand_rank(hand2):
        return 1
    # Find first occurence where hand1 and hand2 differ
    for i in range(5):
        h1 = hand1[i]
        h2 = hand2[i]
        if h1 != h2:
            # Sort by whichever has the highest card label first
            return 2*(label_strength[h1] > label_strength[h2]) - 1
    return 0

from functools import cmp_to_key
sort_hands = cmp_to_key(sort_hands)
# Sort cards using sort_hands
cards.sort(key=lambda x:sort_hands(x[0]))

# hand winnings = value of hand * rank
# Find total winnings
total = 0
for (rank, (_,value)) in enumerate(cards, start=1):
    total += value * rank 
print(total)