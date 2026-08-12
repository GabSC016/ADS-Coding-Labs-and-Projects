# Implement the N-Queens Algorithm

## Objective

Create a program that solves the **N-Queens problem** using Depth-First Search (DFS) and backtracking.

The goal is to place `n` queens on an `n × n` chessboard so that no two queens can attack each other.

The program should find and return **all valid solutions**.

Each solution is represented as a list where the index represents the row and the value represents the column where the queen is placed.

For example:

```text
[1, 3, 0, 2]

. Q . .
. . . Q
Q . . .
. . Q .

If n is less than 1, the function should return an empty list ([]).

Concepts Practiced
Recursion
Depth-First Search (DFS)
Backtracking
Nested functions
Lists
List manipulation (append, pop, copy)
Conditional statements (if)
for loops
range()
Logical operators (and, or)
Checking columns
Checking diagonals
Recursive state management
Base cases
Exploring all possible solutions
Restoring state after recursive calls