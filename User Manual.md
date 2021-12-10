Objective:

In this project, we study the design and application of Constraint Processing (CP) techniques to solve the popular combinatorial game known as the Sudoku puzzle. In particular:
1. We study the modeling of the Sudoku puzzle as a Constraint Satisfaction Problem (CSP).
2. We explore the design and use of CP techniques, both search and constraint propagation, for systematically solving the problem.
3. We develop strategies grounded in CP to dynamically assist a human player solving a Sudoku puzzle.

What is sudoku?

The Sudoku Puzzle was created by Howard Garns in 1979 and originally appeared in the Dell Pencil Puzzles and Word Games magazine. It is sometimes called Number Palace, which was its original name when first published.

This puzzle has 6 lines, 6 columns.

The goal of this puzzle is to place the numbers 1...9 exactly once in each line, column, and block. Some numbers are already given in the cells. We will call these preassigned values.


Approach:

A CSP is defined a 
P =(V,D,C),where
• V = {V1,V2,...,Vn} is a set of n variables.
• D is a set of domains, one domain per variable. The domain DVi of variable Vi is a set of values that Vi can take. And,
C is a set of constraints that apply to the variables. A constraint Ci that applies to a set of variables {Va, Vb, ..., Vk} (called the scope of the constraint) is a relation over the domains of these variables, and specifies the combination of values that the variables can take at the same time.


Sudoku as CSP :

We represent a n × m Sudoku as a CSP as follows:
• Each cell is a CSP variable. There are n2 × m2 variables.
The domain of the cell is the set of values in the interval [1, (n × m)].
If there are n lines and m columns, then the puzzle will have n × m blocks, and there will be n blocks in a line and m lines of blocks. For example, n = 2 and m = 3 is a Sudoku where the variables can take the values [1,6].


Arc-consistency (AC):

The basic operation in arc-consistency is to update the domain of a variable using the Revise operation. This operation revises the domain of one variable given the constraint that links the variable to another variable.

For arc-consistency, we implement AC-3, which revises the domains of all variables until quiescence, revisiting variables that are connected to at least one variable whose domain has been modified.


Sudoku test run Inputs:
010  000  602 000. 260. 003  300. 012. 000. 501. 000  040

Results:

(base) C:\Users\prajw\Downloads\AI Final Project(Sudoku Solver Using Arc Consistency)>python ArcConsistency.py

Input Rules:
 Enter 36 inputs as we are dealing with 6 X 6 sudoku.
 Enter blank spaces with 0 or .


 Enter the Sudoku grid : 003010560320054203206450012045040100

 Solved Sudoku Grid:
4 2 3 |5 1 6
5 6 1 |3 2 4
------+------
1 5 4 |2 6 3
2 3 6 |4 5 1
------+------
3 1 2 |6 4 5
6 4 5 |1 3 2

All constraint tests are passed.

 Hurray!!! sudoku solved in seconds Thanks to Artificial Intelligence.




This is an implementation of Arc Consistency Algorithm to solve a 6x6 Sudoku grid.
