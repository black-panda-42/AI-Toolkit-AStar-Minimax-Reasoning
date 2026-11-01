"""
Heuristic Search Algorithms: A* Search and Grid Navigation.
"""
import heapq
from typing import List, Tuple, Dict, Optional

def a_star_grid(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """A* Search on 2D grid (0 = free cell, 1 = obstacle). Uses Manhattan heuristic."""
    rows, cols = len(grid), len(grid[0])
    def heuristic(p: Tuple[int, int]) -> float:
        return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

    frontier: List[Tuple[float, float, Tuple[int, int]]] = []
    heapq.heappush(frontier, (heuristic(start), 0.0, start))
    came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
    cost_so_far: Dict[Tuple[int, int], float] = {start: 0.0}

    while frontier:
        f_score, g_score, current = heapq.heappop(frontier)
        if current == goal:
            # Reconstruct path
            path = []
            curr = current
            while curr is not None:
                path.append(curr)
                curr = came_from[curr]
            path.reverse()
            return path

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                new_cost = g_score + 1.0
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(neighbor)
                    heapq.heappush(frontier, (priority, new_cost, neighbor))
                    came_from[neighbor] = current
    return None
