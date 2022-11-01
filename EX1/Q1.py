import doctest


def safe_call(f, **kwargs):
    """
    this function verify that the given arguments are similar to the
    annotation of the f function otherwise its raise an error

    :param f: function to check and call
    :param kwargs: count of arguments for  the f function
    :return: the metho retern waht the f function return
    >>> safe_call(f,x=5,y=7.0,z=3)
    15.0
    >>> safe_call(f, x=1, y=-1.0, z=2.0)
    2.0
    """

    if f is None:
        return
    f_parameters = f.__annotations__
    for x, y in kwargs.items():
        if x in f_parameters:
            if type(y) != f_parameters[x]:
                #print(y, x, type(y), f_parameters[x])
                raise Exception(f"The variables doesnt match '{y}' is of type {type(y)}"
                                f" and '{x}' is of type {f_parameters[x]} ")
    return f(**kwargs)


def f(x: int, y: float, z):
    return x+y+z


if __name__ == '__main__':
    doctest.testmod()






