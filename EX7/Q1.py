import numpy as np
import cvxpy as cp
import matplotlib.pyplot as plt
import itertools
import doctest

cvxpy_time = []
numpy_time = []


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        if orig_func.__name__ == 'numpy_linear_eq_solver':
            numpy_time.append(t2)
        else:
            cvxpy_time.append(t2)
        print(f'{ orig_func.__name__} ran in: {t2} sec')
        return result
    return wrapper


@my_timer
def numpy_linear_eq_solver(lhs: np.array, rhs: np.array):
    """
    Method to solve Linear equations using numpy
    :param lhs: left side of the equation
    :param rhs: left side of the equation
    :return: np.array with the solution
    examples:
    >>> numpy_linear_eq_solver(np.array([[1,1],[1.5,4]]), np.array([2200,5050]))
    array([1500.,  700.])
    >>> numpy_linear_eq_solver(np.array([[1,2,3],[0,0,1],[7,8,9]]), np.array([42,10,144]))
    array([ 2.,  5., 10.])

    """
    return np.linalg.solve(lhs, rhs)


@my_timer
def cvxpy_linear_eq_solver(objective, constraints):
    """
    Method to solve Linear equations using cvxpy
    :param objective: function to solve
    :param constraints: constrains for the onjective function
    :return: the solution for the objective function
    examples:
    >>> x = cp.Variable(shape=2)
    >>> '%.2f' % cvxpy_linear_eq_solver(cp.Maximize(cp.sum(x)),[np.array([[1,1],[1.5,4]]) @ x == np.array([2200,5050])])
    '2200.00'
    >>> x = cp.Variable(shape=3)
    >>> l =np.array([[1,4,9],[88,52,-2],[-520,10,3]])
    >>> r = np.array([20,22,11])
    >>> '%.2f' % cvxpy_linear_eq_solver(cp.Maximize(cp.sum(x)),[l @ x == r])
    '2.50'
    """
    return cp.Problem(objective, constraints).solve()


def linear_eq_factory(start: int, end: int, skip: int = 1):
    """
    Method to generate linear equations
    :param start: number of variable to start from
    :param end: number of variable to end
    :param skip: how much to skip between every variable
    """
    for i in range(start, end, skip):
        lhs = np.random.randint(1, 50, size=(i, i))
        rhs = np.random.randint(1, 50, size=i)
        x = cp.Variable(shape=i)
        constraints = [lhs @ x == rhs]
        objective = cp.Maximize(cp.sum(x))
        a = numpy_linear_eq_solver(lhs, rhs)
        b = cvxpy_linear_eq_solver(objective, constraints)
        print(f"numpy solution is: '{np.sum(a)}'")
        print(f"cvxpy solution is: '{b}' \n")
        assert 0.1 > sum(a) - b > -0.1
    cvxpy_vs_numpy_graph(start, end, skip)


def cvxpy_vs_numpy_graph(x_min, x_max, duplicate):
    """
    method that plot the function (time/num of variables) of solving linear equations using
    numpy and cvxpy
    :param x_min: for axis
    :param x_max: for axis
    :param duplicate: duplicate the elements in the array so they fit with the axis
    """
    y_min = min([min(cvxpy_time)-0.1, min(numpy_time)-0.1])
    y_max = max([max(cvxpy_time)+0.1, max(numpy_time)+0.1])
    plt.axis([x_min, x_max, y_min, y_max])
    numpy_f = list(itertools.chain.from_iterable([[elem]*duplicate for elem in numpy_time]))
    cvxpy_f = list(itertools.chain.from_iterable([[elem]*duplicate for elem in cvxpy_time]))

    plt.plot(numpy_f, label=f'numpy - avg time = {sum(numpy_time) / len(numpy_time):.4f}')
    plt.plot(cvxpy_f, label=f'cvxpy - avg time = {sum(cvxpy_time) / len(cvxpy_time):.4f}')
    plt.legend()
    plt.ylabel('Time (seconds)')
    plt.xlabel('Number of Variables')
    plt.title('Linear equations - cvxpy VS numpy')
    plt.show()


if __name__ == '__main__':
    doctest.testmod()
    #linear_eq_factory(2, 50, 3)

