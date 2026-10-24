import math

board = [" "]*9

def win(b, p):
    w = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==p for a,b1,c in w)

def full(b):
    return " " not in b

def ab(b, d, a, beta, mx, stats):
    if win(b,"X"):
        return 1
    if win(b,"O"):
        return -1
    if full(b):
        return 0

    stats[0] = max(stats[0], d)

    if mx:
        v = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                v = max(v, ab(b, d+1, a, beta, False, stats))
                b[i] = " "
                a = max(a, v)
                if beta <= a:
                    stats[1] += 1
                    break
        return v
    else:
        v = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                v = min(v, ab(b, d+1, a, beta, True, stats))
                b[i] = " "
                beta = min(beta, v)
                if beta <= a:
                    stats[1] += 1
                    break
        return v

def best():
    mv = -1
    bestv = -math.inf
    stats = [0,0]
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            v = ab(board, 0, -math.inf, math.inf, False, stats)
            board[i] = " "
            if v > bestv:
                bestv = v
                mv = i
    return mv, stats

def show():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

while True:
    m, stats = best()
    board[m] = "X"
    print("AI move:", m)
    print("depth:", stats[0], "pruned:", stats[1])
    show()
    if win(board,"X") or full(board):
        break

    h = int(input("Enter move (0-8): "))
    if board[h] == " ":
        board[h] = "O"
    show()
    if win(board,"O") or full(board):
        break
