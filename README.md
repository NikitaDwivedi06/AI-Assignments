# AI-Assignments
1) CSP.py

Solves the Graph Colourability Problem by modeling it as a constraint satisfaction problem. Given the adjacency matrix of a graph and the number of colours, this program indicates whether the graph is colouarble by the number of specified colours. If yes, it returns an appropriate assignment.

Heuristics used:
i. To choose the variable for assignment - Minimum Remaining Values, and the Degree Heuristic as a tie breaker
ii. To choose value for assignment - Least Constraining Value Heuristic

Also used Forward Checking

To run: python CSP.py

Input format for the adjacency matrix of a 3 vertex graph: 0 1 1,1 0 1,1 1 0


2) GA.py
Solves the 8 Queens problem by using the Genetic Algorithms technique.
Mutation Probability = 0.0005
Size of initial population = 10

To run: python GA.py

3) ids.py
Solves the 8 tile puzzle problem using Iterative Deepening Search.
Input format (example) for initial state: 1 2 3 4 5 0 7 8 6
0 indicates the blank tile
Goal State: 1 2 3 4 5 6 7 8 0 (Fixed)

To run: python ids.py

