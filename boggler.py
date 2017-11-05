import random
import twl

cubes = [["T", "T", "T", "E", "M", "I"],
        ["M", "E", "E", "U", "A", "G"],
        ["X", "B", "Qu", "K", "J", "Z"],
        ["T", "E", "P", "C", "I", "S"],
        ["O", "O", "O", "U", "T", "T"],
        ["C", "T", "P", "O", "I", "A"],
        ["T", "I", "I", "I", "T", "E"],
        ["H", "H", "O", "R", "D", "L"],
        ["C", "L", "E", "P", "T", "I"],
        ["I", "T", "L", "I", "C", "E"],
        ["S", "S", "S", "U", "N", "E"],
        ["H", "D", "R", "O", "L", "N"],
        ["R", "R", "G", "O", "V", "W"],
        ["F", "A", "A", "A", "R", "S"],
        ["R", "R", "R", "I", "P", "Y"],
        ["E", "E", "E", "E", "A", "M"],
        ["T", "O", "N", "D", "H", "D"],
        ["D", "E", "N", "N", "N", "A"],
        ["P", "R", "F", "I", "Y", "S"],
        ["E", "E", "E", "E", "A", "A"],
        ["F", "A", "I", "R", "Y", "S"],
        ["F", "A", "I", "R", "S", "A"],
        ["S", "E", "N", "T", "C", "C"],
        ["N", "O", "T", "W", "O", "U"],
        ["M", "E", "N", "A", "N", "G"]]

def boggle (cubeset) :
    "generates a big boggle board"
    order = []
    random.shuffle(cubeset)
    for cube in cubeset:
        order.append(random.choice(cube).lower())
    return order

def get_adjacent (cell):
    "returns an array of indices that are adjacent to the given index on a big boggle board"
    #  0  1  2  3  4
    #  5  6  7  8  9
    # 10 11 12 13 14
    # 15 16 17 18 19
    # 20 21 22 23 24
    finalarray = []
    edgetop = False
    edgebot = False
    edgeleft = False
    edgeright = False
    if 0 <= cell <= 4:
        edgetop = True
    if 20 <= cell <= 24:
        edgebot = True
    if cell % 5 == 0:
        edgeleft = True
    if cell % 5 == 4:
        edgeright = True
    if not edgetop:
        if not edgeleft:
            finalarray.append(cell-6)
        finalarray.append(cell-5)
        if not edgeright:
            finalarray.append(cell-4)
    if not edgeleft:
        finalarray.append(cell-1)
    if not edgeright:
        finalarray.append(cell+1)
    if not edgebot:
        if not edgeleft:
            finalarray.append(cell+4)
        finalarray.append(cell+5)
        if not edgeright:
            finalarray.append(cell+6)
    return finalarray

# HERE BEGINS THE SHIT

board = boggle(cubes)

#for space in board:
space = 0

adjs = get_adjacent(space)

#for adj in adjs:
adj = 0

permitted = twl.children(board[space]+board[adj])


