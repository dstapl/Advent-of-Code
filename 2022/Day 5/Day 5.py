def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def read_formation(formation):
    # Each stack element is 3 characters long
    return list(map(lambda x: list(filter(lambda y: y!='   ', x[::-1][1:])), transpose(list(map(lambda s: [s[i:i+3] for i in range(0, len(s), 4)], formation)))))

def read_moves(moves):
    for i in range(len(moves)):
        s = moves[i].split(" from ")
        n = s[0][5:]
        s[1] = s[1].split(" to ")
        a = s[1][0]
        b = s[1][1]
        moves[i] = [int(n), int(a), int(b)]
    return moves
def perform_moves(formation,moves, new=False):
    # move n from a to b
    # Format the moves array
    for move in moves:
        n,a,b = move
        a-=1
        b-=1
        transfer = formation[a][-n:]
        if not(new and len(transfer) > 1):
            transfer = transfer[::-1]
        formation[a] = formation[a][:-n]
        formation[b] += transfer
        #print(formation)
    return formation

def retrieve_top(formation):
    return "".join(map(lambda a: a[-1], formation)).replace("[", "").replace("]", "")
with open("input.txt") as f:
    data = f.read()
    formation, moves = data.split("\n\n")
    formation = formation.split("\n")
    moves = moves.split("\n")
    formation = read_formation(formation)
    moves = read_moves(moves)
    #print(formation)
    formation = perform_moves(formation,moves, True)
    print(retrieve_top(formation))
