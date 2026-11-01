"""
Unit tests for AI-Toolkit search and games.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.search_algorithms import a_star_grid
from src.adversarial import TicTacToeAI

class TestAIToolkit(unittest.TestCase):
    def test_a_star(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        path = a_star_grid(grid, (0, 0), (2, 2))
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))

    def test_tictactoe_win(self):
        # Immediate win available at index 2
        board = [
            'X', 'X', ' ',
            'O', 'O', ' ',
            ' ', ' ', ' '
        ]
        move = TicTacToeAI.find_best_move(board)
        self.assertEqual(move, 2)

if __name__ == "__main__":
    unittest.main()
