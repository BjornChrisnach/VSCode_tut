import math
import extractvar


class Solver:
    def roots(self):
        a = 3
        b = 25
        c = 46
        root1, root2 = self.eval_roots(b, a, c)
        #sqrt = math.sqrt(b**2 - 4 * a * c)
        #root1 = (-b + sqrt) / (2 * a)
        #root2 = (-b - sqrt) / (2 * a)
        return root1, root2

        Solver().demo()

    def eval_roots(self, b, a, c):
        root1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        root2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        return root1, root2
