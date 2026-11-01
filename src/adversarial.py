"""
Adversarial Game Playing: Minimax with Alpha-Beta Pruning for Tic-Tac-Toe.
"""
from typing import List, Tuple, Optional

class TicTacToeAI:
    @classmethod
    def evaluate(cls, board: List[str]) -> int:
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in lines:
            if board[a] != ' ' and board[a] == board[b] == board[c]:
                return 10 if board[a] == 'X' else -10
        return 0

    @classmethod
    def minimax(cls, board: List[str], depth: int, is_max: bool, alpha: int, beta: int) -> int:
        score = cls.evaluate(board)
        if score != 0 or ' ' not in board:
            return score

        if is_max:
            best = -1000
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    best = max(best, cls.minimax(board, depth + 1, False, alpha, beta))
                    board[i] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
            return best
        else:
            best = 1000
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    best = min(best, cls.minimax(board, depth + 1, True, alpha, beta))
                    board[i] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
            return best

    @classmethod
    def find_best_move(cls, board: List[str]) -> int:
        best_val = -1000
        best_move = -1
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                move_val = cls.minimax(board, 0, False, -1000, 1000)
                board[i] = ' '
                if move_val > best_val:
                    best_val = move_val
                    best_move = i
        return best_move
