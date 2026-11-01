# AI-Toolkit: Classical Artificial Intelligence, Heuristic Search & Games

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Domain: Artificial Intelligence](https://img.shields.io/badge/domain-Classical%20AI-blue.svg)]()
[![Academic: BRACU CSE422](https://img.shields.io/badge/course-CSE%20422-orange.svg)]()

## 📌 Course Context: CSE 422 (Artificial Intelligence)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** State-Space Graph Traversal, Informed Heuristic Search (A* Algorithm), Constraint Satisfaction Problems (CSP), and Adversarial Minimax with Alpha-Beta Pruning.

---

## 🎯 AI Algorithms Implemented

1. **A* Heuristic Pathfinding:**
   - Evaluates node priority: $f(n) = g(n) + h(n)$.
   - Employs admissible Manhattan heuristic $h(n) = |x_n - x_g| + |y_n - y_g|$ guaranteeing optimal path discovery through obstacle labyrinths.
2. **Minimax Adversarial Search with $\alpha$-$\beta$ Pruning:**
   - Game tree optimization for 2-player zero-sum games (Tic-Tac-Toe / Connect-4).
   - Prunes search branches whenever $\beta \le \alpha$, reducing search space from $\mathcal{O}(b^d)$ to $\mathcal{O}(b^{d/2})$.

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```
