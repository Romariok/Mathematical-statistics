class Approximation:
    def __init__(self, table):
        assert len(table) == 2
        assert len(table[0]) == len(table[1])
        self.table = table

    def linear(self):
        n = len(self.table[0])
        sx = sum(self.table[0])
        sy = sum(self.table[1])
        sxy = sum([self.table[0][i] * self.table[1][i] for i in range(n)])
        sx2 = sum([self.table[0][i] ** 2 for i in range(n)])
        a = (n * sxy - sx * sy) / (n * sx2 - sx**2)
        b = (sy - a * sx) / n
        return a, b
