import sys
#    | 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 ...
# ----------------------------------------
# 12 |
# 11 |
# 0  |
# 1  |
# 2  |
# 3  |
# 4  |
# 5  |
# 6  |
# 7  |
# 8  |
# 9  |

punchedCardCode = {
    "001000000000":"0", "000100000000":"1", "000010000000":"2", "000001000000":"3", "000000100000":"4",
    "000000010000":"5", "000000001000":"6", "000000000100":"7", "000000000010":"8", "000000000001":"9",
    "100100000000":"A", "100010000000":"B", "100001000000":"C", "100000100000":"D", "100000010000":"E",
    "100000001000":"F", "100000000100":"G", "100000000010":"H", "100000000001":"I",
    "010100000000":"J", "010010000000":"K", "010001000000":"L", "010000100000":"M", "010000010000":"N",
    "010000001000":"O", "010000000100":"P", "010000000010":"Q", "010000000001":"R",
    "001010000000":"S", "001001000000":"T", "001000100000":"U", "001000010000":"V", "001000001000":"W",
    "001000000100":"X", "001000000010":"Y", "001000000001":"Z",
    "000001000010":"#", "001001000010":",", "010001000010":"$", "100001000010":".", "010000000000":"-",
    "000000100010":"@", "001000100010":"%", "010000100010":"*", "100000100010":"<", "001100000000":"/",
    "100000001010":"+", "001000010010":"_", "100000000110":"!", "100000000000":"&", "001000001010":">",
    "000010000010":":", "010000001010":";", "001000000110":"?", "000000000110":'"', "000000001010":"=",
    "010010000010":"!", "100000010010":"("
    }

def initializePunchedCard():
    columns, lines = 80, 12;
    punchedCard = [[0 for x in range(columns)] for y in range(lines)] 
    return punchedCard


def readPunchedCardFile(punchedCardFile, punchedCard):
    with open(punchedCardFile) as f:
        matrix = f.readlines()
    matrix = [x.strip() for x in matrix]
    line = 0
    column = 0
    for l in matrix:
        for c in l:
            punchedCard[line][column] = c
            column = column + 1
        column = 0
        line = line + 1 
    return punchedCard
        

def decodePunchedCard(punchedCard):
    value = ""
    for column in range(80):
        for line in range(12):
            value = value + str(punchedCard[line][column])
        try:
            print(punchedCardCode[value], end="")
        except KeyError as e:
            print(e, file=sys.stderr)
        value = ""


def main():
    punchedCardFile = "<file with punchedCard encoded like shown at top>"
    punchedCard = initializePunchedCard()
    punchedCard = readPunchedCardFile(punchedCardFile, punchedCard)
    decodePunchedCard(punchedCard)


if __name__ == '__main__':
    main()
    