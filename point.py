
class Point:

    def __init__(self, x: int, y: int):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y

    def __hash__(self):
        return (self.X, self.Y).__hash__()

    def __str__(self):
        return f'({self.X}, {self.Y})'

    def __copy__(self):
        return Point(self.X, self.Y)

    def __deepcopy__(self, memo):
        return Point(self.X, self.Y)
