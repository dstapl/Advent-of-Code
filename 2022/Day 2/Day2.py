def part1(game_string):
    score = 0
    outcome_dict = {"A": {"X": 3, "Y": 6, "Z": 0},
                     "B": {"X": 0, "Y": 3, "Z": 6},
                     "C": {"X": 6, "Y": 0, "Z": 3}}
    move_dict = {"X":1,"Y":2,"Z":3}
    for i in game_string.split("\n"):
        opponent, player = i.split()
        score += outcome_dict[opponent][player] + move_dict[player]
    return score


def part2(game_string):
    score = 0
    outcome_dict = {"X": 0, "Y": 3, "Z": 6}
    move_dict = [{"A": 3, "B":1, "C":2},None,None,
                 {"A":1,"B":2,"C":3},None,None,
                 {"A":2,"B":3,"C":1}]
    for i in game_string.split("\n"):
        opponent, outcome = i.split()
        outcome_value = outcome_dict[outcome]
        score += outcome_value + move_dict[outcome_value][opponent]
    return score
with open(r"C:\Users\blamb\OneDrive\Documents\INPUT.txt", "r") as f:
    game = f.read()[:-1]

#print(part1(game))
print(part2(game))
