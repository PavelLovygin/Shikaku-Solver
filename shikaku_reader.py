class shikaku_reader:

    @staticmethod
    def read_matrices_from_file(file_name):
        matrices = []
        with open(file_name, 'r') as file:
            matrix = []
            for line in file:
                if len(line) == 1:
                    matrices.append(matrix)
                    matrix = []
                else:
                    row_str = line[:-1].replace('_', '0')
                    row = [int(x) for x in row_str.split()]
                    matrix.append(row)
            matrices.append(matrix)

        return matrices

    @staticmethod
    def read_matrix_from_console():
        n = int(input('Write dimension:'))
        matrix = []
        for i in range(n):
            row_str = input().replace('_', '0')
            row = [int(x) for x in row_str.split()]
            matrix.append(row)

        return matrix