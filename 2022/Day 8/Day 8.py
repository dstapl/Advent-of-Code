def byRow(string, rowLength):
    return [string[i:i+rowLength] for i in range(0, len(string), rowLength)]


def byColumn(string, rowLength, columnLength):
    return [string[i::columnLength] for i in range(0, rowLength)]

def formatLayout(string, rowLength, columnLength, orientation=False):
    # False = byRow === readliness
    stringArray = byColumn(string, rowLength, columnLength) if orientation else byRow(string, rowLength)
    return map(lambda l: list(map(int,l)), map(list, stringArray))

with open("input_example.txt") as f:
    layout = f.read()
    width = layout.find("\n")
    layout = layout.replace("\n", "")
    height = len(layout)//width
    print(list(formatLayout(layout, width, height, True)))
