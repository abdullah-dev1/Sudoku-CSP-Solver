import time
from collections import deque

# CSP Board

def read_board(filename):
    board = []
    file = open(filename, "r")

    for line in file:
        line = line.strip()
        if line != "":
            row = []
            for ch in line:
                row.append(int(ch))
            board.append(row)

    file.close()
    return board


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("---------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

        print()


# CSP Peers

def get_peers(row, col):
    peers = set()

    for c in range(9):
        if c != col:
            peers.add((row, c))

    for r in range(9):
        if r != row:
            peers.add((r, col))

    start_r = (row // 3) * 3
    start_c = (col // 3) * 3

    for r in range(start_r, start_r + 3):
        for c in range(start_c, start_c + 3):
            if r != row or c != col:
                peers.add((r, c))

    return peers


def build_peers():
    peers = {}
    for r in range(9):
        for c in range(9):
            peers[(r, c)] = get_peers(r, c)
    return peers

# Domains

def build_domains(board, peers):
    domains = {}

    for r in range(9):
        for c in range(9):

            if board[r][c] != 0:
                domains[(r, c)] = {board[r][c]}
            else:
                used = set()

                for (pr, pc) in peers[(r, c)]:
                    if board[pr][pc] != 0:
                        used.add(board[pr][pc])

                possible = set()

                for num in range(1, 10):
                    if num not in used:
                        possible.add(num)

                domains[(r, c)] = possible

    return domains


# AC-3 Algorithm

def ac3(domains, peers):
    queue = deque()

    for cell in domains:
        for neighbor in peers[cell]:
            queue.append((cell, neighbor))

    while len(queue) > 0:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):

            if len(domains[xi]) == 0:
                return False

            for xk in peers[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True


def revise(domains, xi, xj):
    revised = False

    values = list(domains[xi])

    for v in values:
        if domains[xj] == {v}:
            domains[xi].remove(v)
            revised = True

    return revised


# Forward Checking

def forward_check(domains, peers, cell, value):
    removed = []

    for neighbor in peers[cell]:
        if value in domains[neighbor]:
            domains[neighbor].remove(value)
            removed.append((neighbor, value))

            if len(domains[neighbor]) == 0:
                return False, removed

    return True, removed


def restore(domains, removed):
    for (cell, value) in removed:
        domains[cell].add(value)


# Most Remaining Value

def select_variable(assignment, domains):
    unassigned = []

    for cell in domains:
        if cell not in assignment:
            unassigned.append(cell)

    best = unassigned[0]

    for cell in unassigned:
        if len(domains[cell]) < len(domains[best]):
            best = cell

    return best

# Backtracking Algorithm

def is_safe(cell, value, assignment, peers):
    for neighbor in peers[cell]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True


def backtrack(assignment, domains, peers, stats):
    stats["calls"] += 1

    if len(assignment) == 81:
        return assignment

    cell = select_variable(assignment, domains)

    values = list(domains[cell])
    values.sort()

    for value in values:

        if is_safe(cell, value, assignment, peers):
            assignment[cell] = value

            ok, removed = forward_check(domains, peers, cell, value)

            if ok:
                result = backtrack(assignment, domains, peers, stats)
                if result is not None:
                    return result

            del assignment[cell]
            restore(domains, removed)

    stats["failures"] += 1
    return None


# Soduku Solver

def solve(filename):
    print("\nSolving:", filename)

    board = read_board(filename)

    print("\nInitial Board:")
    print_board(board)

    peers = build_peers()
    domains = build_domains(board, peers)

    if not ac3(domains, peers):
        print("No solution exists")
        return

    assignment = {}

    for cell in domains:
        if len(domains[cell]) == 1:
            assignment[cell] = list(domains[cell])[0]

    stats = {"calls": 0, "failures": 0}

    start = time.time()
    result = backtrack(assignment, domains, peers, stats)
    end = time.time()

    if result is None:
        print("No solution found")
    else:
        solved = [[0 for _ in range(9)] for _ in range(9)]

        for (r, c) in result:
            solved[r][c] = result[(r, c)]

        print("\nSolved Board:")
        print_board(solved)

    print("\nBacktrack calls:", stats["calls"])
    print("Backtrack failures:", stats["failures"])
    print("Time:", round(end - start, 3), "seconds")

    if stats["failures"] == 0:
        print("Solved without backtracking.")
    elif stats["failures"] < 10:
        print("Very efficient solving.")
    elif stats["failures"] < 100:
        print("Moderate difficulty.")
    else:
        print("Hard puzzle requiring heavy search.")

# Soduku Solver Board Files

files = ["easy.txt", "medium.txt", "hard.txt", "veryhard.txt"]

for f in files:
    print('\n-------------------------------------------------------------')
    print()
    solve(f)
    print()