def evaluate(boardPosition, maximizingplayer):
    evaluationBoard = ([[0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0]])
    # if value < 6:
    #     print(f"MOVE:{i}")
    #     count[i] += 1
   
def make_move(col):
        pass

def check_horizontal(boardPosition, row, player):
    connect = 0
    
    for num in boardPosition[row]:

        if connect == 4:
            return connect
        if num == player:
            connect += 1

        else:
            connect = 0

    return connect
       
def check_vertical(boardPosition, col, player):
    connect = 0
    i = 0

    while i < 6:
        if connect == 4:
            return connect

        if boardPosition[i][col] == player:
            connect += 1

        else:
            connect = 0
        i += 1

    return connect

def check_diagonal(boardPosition, row, col, player):
    print(f"row: {row}")
    print(f"col: {col}")
    row_start = max(0, (row - col))
    col_start = max(0, (col - row))
    print(f"row start: {row_start}")
    print(f"col start: {col_start}")
    
    height = 6
    width = 7

    connect = 0

    while row_start < height and col_start < width:
        print(boardPosition[row_start][col_start])
        if connect == 4:
            return connect
        if boardPosition[row_start][col_start] == player:
            
            connect += 1
            print(f"connect {connect}")
        else:
            connect = 0

        row_start += 1
        col_start += 1
    return connect

def check_otherdiagonal(boardPosition, row, col, player):
    height = 5
    width = 6
    connect = 0
    distance = height - row

    col_start = max(0, (col - distance))

    row_start = min(5, (row + col))

    while row_start >= 0 and col_start <= width:
        print(boardPosition[row_start][col_start])
        if connect == 4:
            return connect
        if boardPosition[row_start][col_start] == player:
            
            connect += 1
            print(f"connect {connect}")
        else:
            connect = 0

        row_start -= 1
        col_start += 1
    return connect

def is_terminal(boardPosition, row, col, player):
    terminal = False
    for num in boardPosition[0]:
        if num == 0:
            terminal = False


    if check_horizontal(boardPosition, row, player) == 4:
        terminal = True
    if check_vertical(boardPosition, col, player) == 4:
        terminal = True
    if check_diagonal(boardPosition, row, col, player) == 4:
        terminal = True
    if check_otherdiagonal(boardPosition, row, col, player) == 4:
        terminal = True
    return terminal

    

# def minimax(boardPosition, depth, maximizingPlayer):
#     if depth == 0 or is_terminal():
        
#         return boardPosition

    # if maximizingPlayer:
    #     maxEval = float('-inf')
    #     for i, value in enumerate(boardPosition):
    #         eval = minimax(position, depth - 1, False) 
    #         maxEval = max(maxEval, eval)
    #     return maxEval

    # else:
    #     minEval = float('inf')
    #     for position in boardPosition:
    #         eval = minimax(position, depth -1, True)
    #         minEval = min(minEval, eval)
    #     return minEval


