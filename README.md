# AI-Assignments
1) CSP.py

Solves the Graph Colourability Problem by modeling it as a constraint satisfaction problem. Given the adjacency matrix of a graph and the number of colours, this program indicates whether the graph is colouarble by the number of specified colours. If yes, it returns an appropriate assignment.

Heuristics used: <br/>
i. To choose the variable for assignment - Minimum Remaining Values, and the Degree Heuristic as a tie breaker <br/>
ii. To choose value for assignment - Least Constraining Value Heuristic

Also used Forward Checking

To run: python CSP.py

Input format for the adjacency matrix of a 3 vertex graph: 0 1 1,1 0 1,1 1 0


2) GA.py

Solves the 8 Queens problem by using the Genetic Algorithms technique.<br/>
Mutation Probability = 0.0005 <br/>
Size of initial population = 10 <br/>

To run: python GA.py

3) aStar.py
Solves the 8 tile puzzle problem using A-Star Search Technique <br/>
Input format (example) for initial state: 1 2 3 4 5 0 7 8 6 <br/>
0 indicates blank tile <br/>
Goal State: 1 2 3 4 5 6 7 8 0 (Fixed) <br/>

To run: python aStar.py (requires Utilities.py)


4) ids.py

Solves the 8 tile puzzle problem using Iterative Deepening Search.<br/>
Input format (example) for initial state: 1 2 3 4 5 0 7 8 6 <br/>
0 indicates the blank tile <br/>
Goal State: 1 2 3 4 5 6 7 8 0 (Fixed)

To run: python ids.py (requires Utilities.py)


