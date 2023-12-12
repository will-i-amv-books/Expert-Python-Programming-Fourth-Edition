from numbers import Number


class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("All matrix rows must be the same length")
        self.rows = rows

    def __add__(self, other):
        if (
            len(self.rows) != len(other.rows) or 
            len(self.rows[0]) != len(other.rows[0])
        ):
            raise ValueError("Matrix dimensions don't match")
        if isinstance(other, Matrix):
            return Matrix([
                [
                    a + b 
                    for a, b in zip(a_row, b_row)
                ]
                for a_row, b_row in zip(self.rows, other.rows)
            ])
        elif isinstance(other, Number):
            return Matrix([[item + other for item in row] for row in self.rows])
        else:
            raise TypeError(f"Can't add {type(other)} to Matrix")

    def __sub__(self, other):
        if (
            len(self.rows) != len(other.rows) or 
            len(self.rows[0]) != len(other.rows[0])
        ):
            raise ValueError("Matrix dimensions don't match")
        if isinstance(other, Matrix):
            return Matrix([
                [
                    a - b 
                    for a, b in zip(a_row, b_row)
                ]
                for a_row, b_row in zip(self.rows, other.rows)
            ])
        elif isinstance(other, Number):
            return Matrix([[item - other for item in row] for row in self.rows])
        else:
            raise TypeError(f"Can't subtract {type(other)} from Matrix")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if len(self.rows[0]) != len(other.rows):
                raise ValueError("Matrix dimensions don't match")
            rows = [
                [0 for _ in other.rows[0]] 
                for _ in self.rows
            ]
            for i in range(len(self.rows)):
                for j in range(len(other.rows[0])):
                    for k in range(len(other.rows)):
                        rows[i][j] += self.rows[i][k] * other.rows[k][j]
            return Matrix(rows)
        elif isinstance(other, Number):
            return Matrix([[item * other for item in row] for row in self.rows])
        else:
            raise TypeError(f"Can't multiply {type(other)} with Matrix")

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.rows == other.rows
        return super().__eq__(other)

    def __rmul__(self, other):
        if isinstance(other, Number):
            return self * other

    def __repr__(self):
        return "\n".join(str(row) for row in self.rows)


if __name__ == "__main__":
    m0 = Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])
    m1 = Matrix([
        [1, 2, 3],
        [4, 1, 4],
        [5, 7, 9],
    ])
    assert (m1 * m0).rows == m1.rows
    print(f'Matrix m1: \n{m1}\n')
    m2 = Matrix([
        [1, 2, 3],
        [1, 4, 3],
        [1, 0, 5],
    ])
    assert (m2 * m0).rows == m2.rows
    print(f'Matrix m2: \n{m2}\n')
    m1_doubled = m1 * 2
    print(f'Multiplication of m1 by 2: \n{m1_doubled}\n')
    assert m1_doubled == m1 + m1
    assert m1_doubled == 2 * m1
    m2_tripled = m2 * 3
    print(f'Multiplication of m2 by 3: \n{m2_tripled}\n')
    assert m2_tripled ==  m2 + m2 + m2
    assert m2_tripled == 3 * m2
