import os
from copy import deepcopy
from pathlib import Path
from shikaku_reader import shikaku_reader
from shikaku_solver import shikaku_solver

if __name__ == '__main__':
    problem_matrices = shikaku_reader.read_matrices_from_file('tests')
    for problem_matrix in problem_matrices:
        n = len(problem_matrix)
        solver = shikaku_solver(problem_matrix)
        solves = solver.get_solve()

        #for solve in solves:
        for i in range(n):
            for j in range(n):
                print(solves[i][j], end='\t')
            print()
        print()
        #print('\n\n')

    print(True)
