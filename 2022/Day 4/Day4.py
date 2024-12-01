def is_contained(range1, range2):
    range1_start, range1_end = list(map(int,range1.split('-')))
    range2_start, range2_end = list(map(int, range2.split('-')))
    if range1_start <= range2_start and range2_end <= range1_end:
        return True
    elif range2_start <= range1_start and range1_end <= range2_end:
        return True
    else:
        return False

def overlapping(range1, range2):
    range1_start, range1_end = list(map(int,range1.split('-')))
    range1 = range(range1_start, range1_end+1)
    range2_start, range2_end = list(map(int, range2.split('-')))
    range2 = range(range2_start, range2_end+1)
    return set(range1).intersection(set(range2))
with open("input_example.txt", "r") as f:
    data = map(lambda s: s.split(","),f.readlines())
    # # Part 1
    # data = list(map(lambda a: is_contained(*a), data))
    # print(len(list(filter(lambda x: x, data))))

    # Part 2
    data = list(map(lambda a: overlapping(*a), data))
    data = list(filter(None, data))
    data = [item for sublist in map(list, data) for item in sublist]
    print(data)
    unique = set(filter(lambda e:data.count(e)==1, data))
    print(unique)
    for element in unique:
        data.remove(element)
    #data = data[0].intersection(*data[1:])
    #print(len(data))
    print(set(data))
