from functools import reduce

# Create a list of characters that appear in both substrings
def find_common_character(line):
    # Split the line into two substrings
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]

    # Create a list of characters that appear in both substrings
    common_characters = set()
    for character in first_half:
        if character in second_half:
            common_characters.add(character)

    return list(common_characters)[0]

def find_badge(lines):
    # lines = [s1,s2,s3]
    unique_characters = list(map(lambda s: set(s), lines))
    badge = unique_characters[0].intersection(*unique_characters[1:])
    if len(badge) == 2:
        badge.remove("\n")
    return list(badge)[0]
    
# Find the total value of the listed characters, in the entire text file
def find_common_character_lines(lines):
    return map(find_common_character, lines)

def character_value(c):
    if c.islower():
        return ord(c) - 96
    else:
        return ord(c) - 38
                
def find_total_value(lines):
    total_value = 0
    common_characters = find_common_character_lines(lines)
    map(character_value, common_characters)
    for line in lines:
        common_characters = find_common_character(line)
        for character in common_characters:
            total_value += character_value

    return total_value

def find_total_badge_value(lines):
    total_value = 0
    # Iterate 3 at a time
    for group in zip(*[iter(lines)]*3):
        badge = find_badge(group)
        total_value += character_value(find_badge(group))
    return total_value
with open('input.txt', 'r') as f:
    # Read the file
    lines = f.readlines()



# Print the total value
print(find_total_badge_value(lines))
