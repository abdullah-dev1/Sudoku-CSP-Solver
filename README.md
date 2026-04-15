# Sudoku CSP Solver (Artificial Intelligence)

## Overview
This project implements a Sudoku solver using the Constraint Satisfaction Problem (CSP) approach.  
The solver applies advanced AI techniques to efficiently solve Sudoku puzzles of varying difficulty levels.

## Techniques Used
- Backtracking Search
- Forward Checking
- AC-3 (Arc Consistency Algorithm)
- MRV (Minimum Remaining Values) Heuristic

## Problem Description
The goal is to solve Sudoku boards by modeling them as CSPs where:
- Each cell is a variable
- Domain of each variable is {1–9}
- Constraints ensure no repetition in rows, columns, and 3×3 subgrids

## Input Format
- Each Sudoku board is read from a text file
- File contains exactly 9 lines
- Each line contains exactly 9 digits (0–9)
- 0 represents an empty cell

### Example (easy.txt)

004030050

609400000

005100489

000060930

300807002

026040000

453009600

000004705

090050200


## Files Included
- `sudoku.py` → Main CSP solver
- `easy.txt` → Easy puzzle
- `medium.txt` → Medium puzzle
- `hard.txt` → Hard puzzle
- `veryhard.txt` → Very hard puzzle

## How to Run
Run the Python file:

```bash
python sudoku.py


