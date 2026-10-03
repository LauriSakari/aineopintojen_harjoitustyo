def evaluate(history):
    row, col = history[-1]
    evaluationBoard = ([[10,15,20,30,20,15,10],
                        [10,15,20,30,20,15,10],
                        [10,15,20,30,20,15,10],
                        [10,15,20,30,20,15,10],
                        [10,15,20,30,20,15,10],
                        [10,15,20,30,20,15,10]])
    return evaluationBoard[row][col]
   

def check_horizontal(boardPosition, history, player):
    connect = 0
    best_connect = 0
    row, _ = history[-1]

    for num in boardPosition[row]:

        if connect == 4:
            return connect
        if num == player:
            connect += 1
        else:
            best_connect = max(connect, best_connect)
            connect = 0

    return max(connect, best_connect)
       
def check_vertical(boardPosition, history, player):
    _, col = history[-1]
    connect = 0
    best_connect = 0
    i = 0

    while i < 6:
        if connect == 4:
            return connect

        if boardPosition[i][col] == player:
            connect += 1

        else:
            best_connect = max(connect, best_connect)
            connect = 0

        i += 1

    return max(connect, best_connect)

def check_diagonal(boardPosition, history, player):
    row, col = history[-1]
    row_start = max(0, (row - col))
    col_start = max(0, (col - row))
    
    height = 6
    width = 7

    connect = 0
    best_connect = 0

    while row_start < height and col_start < width:
        if connect == 4:
            return connect
        if boardPosition[row_start][col_start] == player:
            connect += 1

        else:
            best_connect = max(connect, best_connect)
            connect = 0

        row_start += 1
        col_start += 1
    return max(connect, best_connect)

def check_otherdiagonal(boardPosition, history, player):
    row, col = history[-1]
    height = 5
    width = 6
    connect = 0
    best_connect = 0
    distance = height - row

    col_start = max(0, (col - distance))

    row_start = min(5, (row + col))

    while row_start >= 0 and col_start <= width:
        if connect == 4:
            return connect
        if boardPosition[row_start][col_start] == player:
            connect += 1
        else:
            best_connect = max(connect, best_connect)
            connect = 0

        row_start -= 1
        col_start += 1
    return max(connect, best_connect)

def evaluate_connections(connect):
    if connect == 4:
        return 100000
    if connect == 3:
        return 5000
    if connect == 2:
        return 100
    else:
        return 0

def is_terminal(boardPosition, history, player):
    if not history:
        return False
    
    player_number = 1
    if player == False:
        player_number = 2

    connections = (
            check_horizontal(boardPosition, history, player_number),
            check_vertical(boardPosition, history, player_number),
            check_diagonal(boardPosition, history, player_number),
            check_otherdiagonal(boardPosition, history, player_number)
    )

    return any(connection >= 4 for connection in connections)

    # slot_evaluation = evaluate(history)

    # evaluation_sum = horizontal + vertical + diag1 + diag2 + slot_evaluation
    # # if check_vertical(boardPosition, history, player_number) == 4:
    # #     terminal = True
    # # if check_diagonal(boardPosition, history, player_number) == 4:
    # #     terminal = True
    # # if check_otherdiagonal(boardPosition, history, player_number) == 4:
    # #     terminal = True
   
    # row, col = history[-1]
    
    # if player_number == 2:
    #     evaluation_sum = evaluation_sum * -1

    # return evaluation_sum, (row, col)

def valid(row):
    if row < 0:
        return False
    return True
    

def minimax(boardPosition, history, next_row_by_column, depth, maximizingPlayer):
    if history:
        last_player = not maximizingPlayer
        if is_terminal(boardPosition, history, last_player):
            score = 100000 if last_player else -100000
            return score, history[-1]
        if all(not valid(row) for row in next_row_by_column):
            return 0, None
        
    if depth == 0:
        return evaluate(history), history[-1]

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for col, row in enumerate(next_row_by_column):
            if not valid(row):
                continue
            boardPosition[row][col] = 1
            history.append((row, col))
            next_row_by_column[col] = next_row_by_column[col] - 1
            eval, _ = minimax(boardPosition, history, next_row_by_column, depth - 1, False) 
            if eval > maxEval:
                maxEval = eval
                best_move = (row, col)
            history.pop()
            boardPosition[row][col] = 0
            next_row_by_column[col] = next_row_by_column[col] + 1
            
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for col, row in enumerate(next_row_by_column):
            if not valid(row):
                continue
            boardPosition[row][col] = 2
            history.append((row, col))
            next_row_by_column[col] = next_row_by_column[col] - 1
            eval, _ = minimax(boardPosition, history, next_row_by_column, depth - 1, True)
            if eval < minEval:
                minEval = eval
                best_move = (row, col)
            history.pop()
            boardPosition[row][col] = 0
            next_row_by_column[col] = next_row_by_column[col] + 1
            
        return minEval, best_move

