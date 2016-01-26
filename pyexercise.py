import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.ln(x) * sy.exp(-x**2), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array([
    [5, 1, 6, 5, 9, 1, 6, 3, 0, 6],
    [9, 2, 7, 7, 8, 2, 4, 8, 4, 1],
    [1, 2, 0, 4, 0, 3, 1, 1, 6, 8],
    [0, 6, 3, 7, 8, 6, 8, 5, 9, 8],
    [1, 3, 0, 3, 4, 2, 0, 5, 7, 3],
    [7, 5, 4, 3, 3, 3, 0, 0, 3, 3],
    [5, 1, 2, 2, 4, 5, 8, 9, 2, 2],
    [7, 8, 0, 2, 2, 9, 8, 6, 2, 4],
    [3, 7, 4, 8, 2, 3, 2, 0, 1, 6],
    [3, 9, 1, 1, 4, 0, 6, 1, 6, 1]])
    b = np.array([91, 71, 97, 87, 67, 35, 81, 19, 72, 13])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1307304
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())

