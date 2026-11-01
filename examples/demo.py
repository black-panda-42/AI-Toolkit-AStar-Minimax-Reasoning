"""
Demonstration of AI-Toolkit: A* Grid Pathfinding and Alpha-Beta Adversarial Search.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.search_algorithms import a_star_grid
from src.adversarial import TicTacToeAI

def main():
    print("=" * 65)
    print("       AI-TOOLKIT: HEURISTIC SEARCH & ADVERSARIAL REASONING   ")
    print("=" * 65)

    # 1. A* Pathfinding through an obstacle labyrinth
    grid = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)
    path = a_star_grid(grid, start, goal)
    print(f"[+] A* Search Path from {start} to {goal}:")
    print(f"    - Optimal Path Length: {len(path)} steps")
    print(f"    - Waypoint Trajectory: {path}")

    # 2. Minimax with Alpha-Beta Pruning (Optimal move selection)
    # Board: X at 0, O at 4, X at 8 -> O is about to block or X to attack
    board = [
        'X', ' ', ' ',
        ' ', 'O', ' ',
        ' ', ' ', 'X'
    ]
    best_move = TicTacToeAI.find_best_move(board)
    print(f"\n[+] Minimax Alpha-Beta Decision for Tic-Tac-Toe:")
    print(f"    - Current Board: {board[:3]}\n                     {board[3:6]}\n                     {board[6:]}")
    print(f"    - AI ('X') Recommends Move at Index: {best_move} (Row {best_move//3}, Col {best_move%3})")
    print("=" * 65)

if __name__ == "__main__":
    main()
