# Fifteen Game (Python)

This is a Python implementation of the Fifteen Puzzle, a game where the goal is to arrange the tiles in numerical order by sliding them to the around making use of the empty tile spot.

## Play in Browser

Run the game directly in your browser using Replit:

**[Play on Replit](https://replit.com/@hanarjahangiri/fifteen-game)**

---

## Files in Repo

| File             | Description                                                |
|------------------|------------------------------------------------------------|
| `fifteen.py`     | Core game logic (tile board, valid moves, win check)       |
| `game.py`        | Tkinter-based GUI — main file to run and play the game     |
| `pqueue.py`      | Custom priority queue used for solving or AI logic         |
| `permutation.py` | Checks solvability and handles permutation generation      |
| `graph_quiz.py`  | Optional graph quiz logic for extra features               |
| `graph.py`       | Graph traversal and utility functions                      |
| `treemax.py`     | Binary tree helper functions (e.g., max value search)      |
| `final.ipynb`    | Notebook for testing and experimenting with game logic     |

---

## How to Run Locally (Requires: Python3, Tkinter)

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/fifteen-game.git
   cd fifteen-game
   ```
2. Run the game  
   ```bash
   python3 game.py
   ```