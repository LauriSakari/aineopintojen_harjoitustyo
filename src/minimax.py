import time

def evaluate(board_position, history, player):
    
    player_number = 1
    if player == False:
        player_number = 2
    row, col = history[-1]

    evaluationBoard = ([[5,10,15,20,15,10,5],
                        [5,10,15,20,15,10,5],
                        [5,10,20,30,20,10,5],
                        [5,10,30,40,30,10,5],
                        [5,10,20,30,20,10,5],
                        [5,10,15,20,15,10,5]])
    
    score = evaluationBoard[row][col]

    connections = (
        check_horizontal(board_position, history, player_number),
        check_vertical(board_position, history, player_number),
        check_diagonal(board_position, history, player_number),
        check_otherdiagonal(board_position, history, player_number)
    )

    for connection in connections:
        score += evaluate_connections(connection)

    if player_number == 2:
        score = score * -1
    return score
   

def check_horizontal(board_position, history, player):
    connect = 0
    best_connect = 0
    row, _ = history[-1]

    for num in board_position[row]:

        if connect == 4:
            return connect
        if num == player:
            connect += 1
        else:
            best_connect = max(connect, best_connect)
            connect = 0

    return max(connect, best_connect)
       
def check_vertical(board_position, history, player):
    _, col = history[-1]
    connect = 0
    best_connect = 0
    i = 0

    while i < 6:
        if connect == 4:
            return connect

        if board_position[i][col] == player:
            connect += 1

        else:
            best_connect = max(connect, best_connect)
            connect = 0

        i += 1

    return max(connect, best_connect)

def check_diagonal(board_position, history, player):
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
        if board_position[row_start][col_start] == player:
            connect += 1

        else:
            best_connect = max(connect, best_connect)
            connect = 0

        row_start += 1
        col_start += 1
    return max(connect, best_connect)

def check_otherdiagonal(board_position, history, player):
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
        if board_position[row_start][col_start] == player:
            connect += 1
        else:
            best_connect = max(connect, best_connect)
            connect = 0

        row_start -= 1
        col_start += 1
    return max(connect, best_connect)

def evaluate_connections(connect):

    if connect == 3:
        return 5000
    if connect == 2:
        return 100
    else:
        return 0

def is_terminal(board_position, history, player):
    if not history:
        return False
    
    player_number = 1
    if player == False:
        player_number = 2

    connections = (
            check_horizontal(board_position, history, player_number),
            check_vertical(board_position, history, player_number),
            check_diagonal(board_position, history, player_number),
            check_otherdiagonal(board_position, history, player_number)
    )

    return any(connection >= 4 for connection in connections)

    # slot_evaluation = evaluate(history)

    # evaluation_sum = horizontal + vertical + diag1 + diag2 + slot_evaluation
    # # if check_vertical(board_position, history, player_number) == 4:
    # #     terminal = True
    # # if check_diagonal(board_position, history, player_number) == 4:
    # #     terminal = True
    # # if check_otherdiagonal(board_position, history, player_number) == 4:
    # #     terminal = True
   
    # row, col = history[-1]
    
    # if player_number == 2:
    #     evaluation_sum = evaluation_sum * -1

    # return evaluation_sum, (row, col)

def valid(row):
    if row < 0:
        return False
    return True
    

def minimax(board_position, history, next_row_by_column, depth, maximizingPlayer, alpha, beta, starting_move, think_until):
    if time.monotonic() >= think_until:
        raise TimeoutError
    
    if history:
        last_player = not maximizingPlayer
        if is_terminal(board_position, history, last_player):
            print(f"IS TERMINAL!!!!! {history[-1]}")
            score = 100000 if last_player else -100000
            return score, history[-1]
        if all(not valid(row) for row in next_row_by_column):
            print("TASAPELI")
            return 0, None
        
    if depth == 0:
        return evaluate(board_position, history, not maximizingPlayer), history[-1]

    priority_order = [3, 2, 4, 1, 5, 0, 6]

    if starting_move != 3:
        priority_order.remove(starting_move)
        priority_order = [starting_move] + priority_order
        print(f"Priority order{priority_order}!!!!!!!!!!!!!!!!!!!!??????????????????????????????????????")

    if maximizingPlayer:
        maxEval = float('-inf')
        best_move = None
        for i in priority_order:
            row = next_row_by_column[i]
            col = i
            if not valid(row):
                continue
            board_position[row][col] = 1
            history.append((row, col))
            next_row_by_column[col] = next_row_by_column[col] - 1
            try:
                eval, _ = minimax(board_position, history, next_row_by_column, depth - 1, False, alpha, beta, starting_move, think_until) 
                if eval > maxEval:
                    maxEval = eval
                    best_move = (row, col)
            finally:
                history.pop()
                board_position[row][col] = 0
                next_row_by_column[col] = next_row_by_column[col] + 1
            alpha = max(alpha, maxEval) 
            if beta <= alpha:
                break
            
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for i in priority_order:
            row = next_row_by_column[i]
            col = i
            if not valid(row):
                continue
            board_position[row][col] = 2
            history.append((row, col))
            next_row_by_column[col] = next_row_by_column[col] - 1
            try: 
                eval, _ = minimax(board_position, history, next_row_by_column, depth - 1, True, alpha, beta, starting_move, think_until)
                if eval < minEval:
                    minEval = eval
                    best_move = (row, col)
            finally:
                history.pop()
                board_position[row][col] = 0
                next_row_by_column[col] = next_row_by_column[col] + 1
            beta = min(beta, minEval)
            if beta <= alpha:
                break
            
        return minEval, best_move


def calculate_next_move(depth, next_row_by_column, current_state, best_move_of_current_depth, time_limit):
    think_until = time.monotonic() + time_limit
    for current_depth in range(1, depth+1):
        try:
            eval, next_move  = minimax(current_state, [], next_row_by_column, current_depth, False, float('-inf'), float('inf'), best_move_of_current_depth, think_until)
            best_move_of_current_depth = next_move[1]
            print(f"KIERROS {current_depth} LOPPU {best_move_of_current_depth} on paras siirto XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        except TimeoutError:
            break
        
    
    return next_move

