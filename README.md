# Shikaku-Solver
 This project is a solver Shikaku puzzles


######Developer:
Ловыгин Павел
***

###How to use:

The constructor of the `shikaku_solver` class accepts a matrix containing a shikaku puzzle. 
The matrix containing the shikaku puzzle can be obtained from the `shikkaku_reader` class by reading it from the console or from a file. 
Then you need to call the `get_solve()` or `get_all_solves()` method from this class.

### Example:
For example, you can read all the Shikaku tasks from a file named 'test' and find a solution for each
```
problem_matrices = shikaku_reader.read_matrices_from_file('tests')
for problem_matrix in problem_matrices:
    n = len(problem_matrix)
    solver = shikaku_solver(problem_matrix)
    solves = solver.get_solve()
```

To get all possible solutions to the Shikaku problem, use the `get_all_solve()` method