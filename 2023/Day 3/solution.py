file = open(0).read()


def neighbours(idx, line_len):
    mod_idx = idx % line_len
    # Check left wall
    if mod_idx == 0:
        return
    # Check right wall
    if mod_idx == line_len-1:
        return
    # Check top
    if idx < line_len:
        return
    # Check bottom
    if idx:
        return

numbers = [
    # (num, (start_idx, end_idx))
]
symbols = [
    # (symbol, idx)
]



num_group = [
    # (num, idx)
]
for idx, character in enumerate(file, start=0):
    if character.isnumeric(): # Check if digit of a number
        num_group.append((idx, character))
        continue
    elif num_group: # Check if not empty
        # numgroups should be short so sorting will be fine for now
        # num_group.sort(key=lambda x: x[1])
        idxs, nums = zip(*num_group)
        nums = int("".join(nums))
        idxs = list(idxs)
        idxs.sort()
        idxs = (idxs[0], idxs[-1])
        numbers.append((nums, idxs))
        num_group = []
    if character != "." and character != "\n": # Excluded
        symbols.append((character, idx))
    
print(f"{numbers = }")
print(f"{symbols = }")


# Find a symbol --> find neighbours
# If neighbour is a digit, mark idx of digit
# At the end have a list of digits
# Search outwards from digits to find all numbers