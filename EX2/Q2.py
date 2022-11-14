import doctest

func_and_params = {}


def lastcall(f):
    """
    last call is a decorator the get a function and calculate its output
    it save all the parameters and when the function is called with the same parameter
    the decorator print a message saying this parameter was already calculated
    :param f: a function to calculate
    :return: the solution of f(x) or a message if x was already calculated
    >>> f(1)
    1
    >>> f(2)
    4
    >>> f1(10)
    11
    >>> f(1)
    I already told you that the answer is 1!
    >>> f(2)
    I already told you that the answer is 4!
    >>> f1(10)
    I already told you that the answer is 11!
    >>> f2(-10)
    10
    >>> lower_to_upper("amiel")
    'AMIEL'
    >>> lower_to_upper("aMiel")
    'AMIEL'
    >>> lower_to_upper("amiel")
    I already told you that the answer is AMIEL!
    >>> f(2)
    I already told you that the answer is 4!
    >>> f(3)
    9
    >>> f2(10)
    10
    >>> f2(-10)
    I already told you that the answer is 10!

    """
    def wrapper(*args):
        func_name = f.__name__
        param = args[0]
        if func_name in func_and_params:
            if param in func_and_params[func_name]:
                print(f"I already told you that the answer is {func_and_params[func_name][param]}!")
            else:
                func_and_params[func_name][param] = f(*args)
                return func_and_params[func_name][param]
        else:
            func_and_params[func_name] = {}
            func_and_params[func_name][param] = f(*args)
            return func_and_params[func_name][param]
    return wrapper


@lastcall
def f(x: int):
    return x**2


@lastcall
def lower_to_upper(x: str):
    return x.upper()

@lastcall
def f1(x: int):
    return x+1

@lastcall
def f2(x: int):
    return abs(x)


if __name__ == '__main__':
    doctest.testmod()
