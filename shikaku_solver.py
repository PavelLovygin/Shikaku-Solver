
from copy import deepcopy
from point import Point
from rectangle import Rect


class shikaku_solver:

    def __init__(self, matrix):
        self.__problem_matrix = matrix
        self.__point_rect_various = dict()
        self.__unresolved_points = self.__get_start_points()
        self.__reserved_points = deepcopy(self.__unresolved_points)
        self.__ans_matrix = [['0' for j in range(len(matrix))] for i in range(len(matrix))]
        self.__curr_num = 1
        self.__determine_part_solve()

    def get_solve(self):
        if len(self.__unresolved_points) == 0:
            return self.__ans_matrix

        if self.__is_solve_impossible():
            return False

        unresolved_point = list(self.__unresolved_points)[0]
        for poss_rect in self.__point_rect_various[unresolved_point]:
            solver_copy = deepcopy(self)
            #solver_copy.reserve_rect(poss_rect, unresolved_point)
            #solver_copy.determine_part_solve()
            ans = solver_copy.get_solve_with_reversed_rect(poss_rect, unresolved_point)
            if ans:
                return ans

    def get_solve_with_reversed_rect(self, rect: Rect, point: Point):
        self.__reserve_rect(rect, point)
        self.__determine_part_solve()
        return self.get_solve()

    def get_all_solves(self):
        answers = []
        if len(self.__unresolved_points) == 0:
            answers.append(self.__ans_matrix)

        if self.__is_solve_impossible():
            return False

        if len(self.__unresolved_points) != 0:
            unresolved_point = list(self.__unresolved_points)[0]
            for poss_rect in self.__point_rect_various[unresolved_point]:
                solver_copy = deepcopy(self)
                #solver_copy.reserve_rect(poss_rect, unresolved_point)
                #solver_copy.determine_part_solve()
                ans = solver_copy.get_all_solves_with_reversed_rect(poss_rect, unresolved_point)
                if ans:
                    answers.extend(ans)

        return answers

    def get_all_solves_with_reversed_rect(self, rect: Rect, point: Point):
        self.__reserve_rect(rect, point)
        self.__determine_part_solve()
        return self.get_all_solves()

    def __determine_part_solve(self):
        count_only_possible_point_solutions = 1
        while count_only_possible_point_solutions != 0:
            for point in self.__unresolved_points.copy():
                rect_various = self.__get_rect_various(point)
                if len(rect_various) == 1:
                    self.__reserve_rect(list(rect_various)[0], point)
                else:
                    self.__point_rect_various[point] = self.__get_rect_various(point)

            count_only_possible_point_solutions = 0
            for point in self.__unresolved_points:
                if len(self.__point_rect_various[point]) == 1:
                    count_only_possible_point_solutions += 1

    def __get_start_points(self) -> set:
        """Ищет и возвращает множество изначальных точек из Shikaku"""
        points = set()
        for i in range(len(self.__problem_matrix)):
            for j in range(len(self.__problem_matrix[i])):
                if self.__problem_matrix[i][j] != 0:
                    points.add(Point(i, j))

        return points

    def __get_rect_various(self, point: Point) -> set:
        """Возвращает множество допустимых вариантов прямоугольников для данной ячейки"""
        number = self.__problem_matrix[point.X][point.Y]
        rect_various = set()
        n = len(self.__problem_matrix)
        for num in range(1, number + 1):
            if number % num == 0:
                height = num
                width = number // num
                for i in range(max(0, point.X - height + 1), min(point.X + 1, n - height + 1)):
                    for j in range(max(0, point.Y - width + 1), min(point.Y + 1, n - width + 1)):
                        if not self.__is_reserved_points_in_rect(Rect(i, j, height, width), point):
                            rect_various.add(Rect(i, j, height, width))

        return rect_various

    def __is_reserved_points_in_rect(self, rect: Rect, point: Point):
        """Проверят, есть ли в данном прямоугольнике уже занятые клетки"""
        for res_p in self.__reserved_points:
            if rect.contain(res_p) and res_p != point:
                return True
        return False

    def __reserve_rect(self, rect, point: Point):
        """Занимает все клетки для данного прямоугольника"""

        if point in self.__unresolved_points:
            self.__unresolved_points.remove(point)

        new_reserved_points = set()
        for x in range(rect.X, rect.X + rect.Height):
            for y in range(rect.Y, rect.Y + rect.Width):
                if self.__curr_num >= 10:
                    self.__ans_matrix[x][y] = chr(97 + self.__curr_num - 10)
                else:
                    self.__ans_matrix[x][y] = str(self.__curr_num)
                new_reserved_points.add(Point(x, y))
        self.__reserved_points = self.__reserved_points | new_reserved_points
        self.__curr_num += 1

        for problem_p in self.__point_rect_various.keys():
            is_found_conflict = False
            for rect in self.__point_rect_various[problem_p]:
                for res_p in new_reserved_points:
                    if rect.contain(res_p):
                        self.__point_rect_various[problem_p].remove(rect)
                        is_found_conflict = True
                        break
                if is_found_conflict:
                    break

        if point in self.__point_rect_various:
            self.__point_rect_various.pop(point)

    def __is_solve_impossible(self):
        for point in self.__unresolved_points:
            if len(self.__point_rect_various[point]) == 0:
                return True

        return False
