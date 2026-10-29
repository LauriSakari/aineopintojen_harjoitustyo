import unittest, time
from minimax import check_vertical, check_horizontal, check_diagonal, check_otherdiagonal, is_terminal, minimax
from main import calculate_next_move


class TestMinimax(unittest.TestCase):

    def test_check_vertical_recognizes_win(self):
        board = [[0] * 7 for _ in range(6)]

        for row in range(1, 5):
            board[row][2] = 1

        assert check_vertical(board, [(5, 2)], 1) == 4

    def test_check_horizontal_recognizes_win(self):
        board = [[0] * 7 for _ in range(6)]

        for col in range(3, 7):
            board[5][col] = 1

        assert check_horizontal(board, [(5, 6)], 1) == 4

    
    def test_check_diagonal_recognizes_win(self):
        board = [[0] * 7 for _ in range(6)]

        i = 2
        while i < 6:
            board[i][i] = 1
            i += 1

        assert check_diagonal(board, [(2, 2)], 1) == 4

    def test_check_other_diagonal_recognizes_win(self):
        board = [[0] * 7 for _ in range(6)]

        r = 5
        c = 1
        while c < 5:
            board[r][c] = 1
            r -= 1
            c += 1

        assert check_otherdiagonal(board, [(r, c)], 1) == 4

    def test_is_terminalFunction(self):
    
        board = [[0] * 7 for _ in range(6)]

        i = 2
        while i < 6:
            board[i][i] = 1
            i += 1

        assert is_terminal(board, [(2, 2)], True) == True
        assert is_terminal(board, [], True) == False #returns False when no moves in history
        assert is_terminal(board, [(2, 2)], False) == False #returns false when wrong player



    def test_ai_can_block(self):

        board = [[0] * 7 for _ in range(6)]

        board[4][3] = 2
        board[5] = [0,0,2,1,1,1,0]

        depth = 4
        count = [5,5,4,3,4,4,5]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (5,6)

    def test_ai_chooses_to_win_not_block(self):

        board = [[0] * 7 for _ in range(6)]

        for i in range(3, 6):
                board[i] = [0,0,0,2,1,0,0]

        depth = 4
        count = [5,5,5,2,2,5,5]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (2,3)
        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, True) == (2,4)

    def test_ai_chooses_to_win_not_block_2(self):

        board = [[0,1,0,0,0,0,0],
                 [0,1,2,2,0,0,0],
                 [0,2,1,2,1,0,0],
                 [0,1,1,1,2,0,0],
                 [0,2,2,1,2,0,0],
                 [0,2,2,1,1,1,0]]

        depth = 6
        count = [5,-1,0,0,1,4,5]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (4,5)

    def test_ai_chooses_to_open_in_the_middle(self):

        board = [[0] * 7 for _ in range(6)]

        depth = 4
        count = [5,5,5,5,5,5,5]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, True) == (5,3)

    def test_ai_blocks_when_slot_in_the_middle(self):

        board = [[0] * 7 for _ in range(6)]

        board[4] = [1,0,2,2,0,0,0] 
        board[5] = [1,0,1,1,2,0,0]        

        depth = 3
        count = [3,5,3,3,4,5,5]
        best_move_of_current_depth = 3
        time_limit = 5

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (5,1)

    def test_ai_blocks_open_two(self):

        board = [[0] * 7 for _ in range(6)]

        board[2] = [0,0,1,0,0,0,0] 
        board[3] = [0,0,1,0,0,0,0] 
        board[4] = [0,0,2,2,0,0,0] 
        board[5] = [0,0,1,1,0,0,0]        

        depth = 3
        count = [5,5,1,3,5,5,5]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (5,1) or (5,4)

    def test_algorithm_handles_full_board(self):
        
        board = [
            [1,2,1,2,1,2,1],     
            [1,2,1,2,1,2,1],
            [1,2,1,2,1,2,1],
            [2,1,2,1,2,1,2],
            [2,1,2,1,2,1,2],
            [2,1,2,1,2,1,2]]


        depth = 3
        count = [-1,-1,-1,-1,-1,-1,-1]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False) == (0, None)
        thinking_time = time.monotonic() + 0.2
        assert minimax(board, [(0,1)], count, depth, True, 3, 10, best_move_of_current_depth, thinking_time) == (0, None)
        
    def test_full_col_is_recognized_in_minimax(self):

        board = [[0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,0,1,0,0,0],
                 [0,0,0,2,0,0,0],
                 [0,0,0,2,0,0,0],
                 [0,0,0,1,0,0,0]]
        
        depth = 3
        count = [0,0,0,-1,0,0,0]
        best_move_of_current_depth = 3
        time_limit = 2

        assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, True)[1] != 3

    def test_timeout_error_is_raised(self):

        board = [[0] * 7 for _ in range(6)]

        depth = 3
        count = [0,0,0,0,0,0,0]
        best_move_of_current_depth = 3
        time_limit = -1
        thinking_time = time.monotonic() - 0.2
        try:
            assert minimax(board, [], count, depth, True, 3, 10, best_move_of_current_depth, thinking_time)
        except TimeoutError:
            assert True

        try:
            assert calculate_next_move(depth, count, board, best_move_of_current_depth, time_limit, False)
        except TimeoutError:
            assert True