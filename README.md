<div align="center">

# 🧩 Sudoku CSP Solver
### *Artificial Intelligence • Constraint Satisfaction Problem (CSP)*

A Python implementation of a **Sudoku Solver** powered by classic **Artificial Intelligence** algorithms.  
The project models Sudoku as a **Constraint Satisfaction Problem (CSP)** and combines multiple constraint propagation techniques with intelligent search heuristics to solve puzzles efficiently.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/Artificial-Intelligence-8A2BE2?style=for-the-badge)
![Algorithm](https://img.shields.io/badge/CSP-Solver-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

# 📖 Overview

This project demonstrates how **Artificial Intelligence** techniques can be applied to solve Sudoku puzzles using the **Constraint Satisfaction Problem (CSP)** framework.

Each Sudoku board is represented as a CSP where every empty cell is treated as a variable with a finite domain. By combining constraint propagation with informed search strategies, the solver efficiently solves puzzles ranging from **Easy** to **Very Hard** difficulty levels.

---

# ✨ AI Techniques Implemented

- 🔍 Backtracking Search
- ⚡ Forward Checking
- 🔗 AC-3 (Arc Consistency Algorithm)
- 🎯 MRV (Minimum Remaining Values) Heuristic

---

# 🧠 CSP Formulation

The Sudoku puzzle is modeled as a Constraint Satisfaction Problem where:

| Component | Description |
|-----------|-------------|
| **Variables** | Individual Sudoku cells |
| **Domain** | Values **1–9** |
| **Constraints** | No duplicate values in any row, column, or 3×3 subgrid |

---

# 📥 Input Format

The solver accepts Sudoku puzzles from a plain text file.

### Requirements

- Exactly **9 lines**
- Exactly **9 digits** per line
- Digits range from **0–9**
- **0** represents an empty cell

### Example (`easy.txt`)

```text
004030050
609400000
005100489
000060930
300807002
026040000
453009600
000004705
090050200
```

---

# 📂 Project Structure

```text
Sudoku-CSP-Solver/
│
├── sudoku.py          # Main CSP Solver
├── easy.txt           # Easy Puzzle
├── medium.txt         # Medium Puzzle
├── hard.txt           # Hard Puzzle
└── veryhard.txt       # Very Hard Puzzle
```

---

# ▶️ Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/Sudoku-CSP-Solver.git
```

### Navigate to the project

```bash
cd Sudoku-CSP-Solver
```

### Run the solver

```bash
python sudoku.py
```

---

# 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Constraint Satisfaction Problems (CSP)
- Constraint Propagation
- Search Algorithms
- Artificial Intelligence Fundamentals
- Heuristic-Based Optimization
- Sudoku Solving using AI

---

<div align="center">

### ⭐ If you found this project helpful, consider giving it a star!

**Built with Python ❤️ using Artificial Intelligence techniques.**

</div>
