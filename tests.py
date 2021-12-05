import os
from copy import deepcopy
from pathlib import Path
from shikaku_reader import shikaku_reader
from shikaku_solver import shikaku_solver


problem_matrices = shikaku_reader.read_matrices_from_file('tests')
solver = shikaku_solver(problem_matrices[0])

solver_copy = deepcopy(solver)
solver.__determine_part_solve()
n = len(solver.__problem_matrix)
for i in range(n):
    for j in range(n):
        print(solver.__ans_matrix[i][j], end='\t')
    print()
print()

for i in range(n):
    for j in range(n):
        print(solver_copy.__ans_matrix[i][j], end='\t')
    print()
print()

'''
def maybe_copy(self):
    new_solver = shikaku_solver(copy.deepcopy(self.problem_matrix))
    new_solver.problem_matrix = copy.deepcopy(self.problem_matrix)
    new_solver.point_rect_various = copy.deepcopy(self.point_rect_various)
    new_solver.unresolved_points = copy.copy(self.unresolved_points)
    new_solver.reserved_points = copy.copy(self.reserved_points)
    new_solver.ans_matrix = copy.deepcopy(self.ans_matrix)
    new_solver.curr_num = self.curr_num
    return new_solver

'''