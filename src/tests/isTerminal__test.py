import unittest
from minimax import check_vertical, check_horizontal, check_diagonal, check_otherdiagonal, is_terminal


class TestIsTerminalChecks(unittest.TestCase):

    def test_check_vertical_recognizes_win(self):
        board = [[0] * 7 for _ in range(6)]

        for row in range(2, 6):
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

    def test_isTerminalFunction(self):
    
        board = [[0] * 7 for _ in range(6)]

        i = 2
        while i < 6:
            board[i][i] = 1
            i += 1

        assert is_terminal(board, [(2, 2)], True) == True
        assert is_terminal(board, [(2, 2)], False) == False #returns false when wrong player

