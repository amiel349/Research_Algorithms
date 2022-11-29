import itertools
import doctest


def bounded_subsets(s: list, c: int, is_sort=False):
    """
    wrapping method for the bounded sort problem
    before calling the right method we sort s and remove every element bigger than c
    :param s: list of integers
    :param c: target number to be the bound of the subsets
    :param is_sort: boolean flag if true the method will return a generator sorted by the sum of
    the value of the subsets
    :return: generator with all the subsets smaller than c
    >>> for x in bounded_subsets([1, 2, 3], 4):
    ...     print(x)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    >>> for x in bounded_subsets([3,2 ,1 ], 4, True):
    ...     print(x)
    []
    [1]
    [2]
    [3]
    [1, 2]
    [1, 3]
    >>> for x in bounded_subsets([], 4, True):
    ...     print(x)
    []
    >>> for x in bounded_subsets([9],8):
    ...     print(x)
    []
    >>> for x in bounded_subsets(range(50,150), 103): # doctest:+ELLIPSIS
    ...      print(x)
    []
    [50]
    [51]
    [52]
    ...
    [102]
    [103]
    [50, 51]
    [50, 52]
    [50, 53]
    [51, 52]
    >>> for x in bounded_subsets(range(50,150), 103, True): # doctest:+ELLIPSIS
    ...      print(x)
    []
    [50]
    [51]
    ...
    [100]
    [101]
    [50, 51]
    [102]
    [50, 52]
    [103]
    [50, 53]
    [51, 52]


    """
    new_s = list(s)
    new_s.sort()
    index = 0
    for i in new_s:
        if i > c:
            break
        index += 1
    if is_sort:
        return bounded_subsets_sorted(new_s[0:index], c)
    return bounded_subsets_not_sorted(new_s[0:index], c)


def bounded_subsets_not_sorted(s, c):
    """
    the method call the generator from itertools than
    it itarate it and every time the generator is called it return the next subset smaller than c
    :param s: list of integers
    :param c: target number to be the bound of the subsets
    :return: generator with all the subsets smaller than c
    """
    size = 1
    sum_of_s = 0
    for i in range(len(s)):
        sum_of_s += s[i]
        size += 1
        if sum_of_s > c:
            break

    for sub_set in itertools.chain.from_iterable(sorted(itertools.combinations(s, r), key=sum) for r in range(size)):
        if sum(sub_set) <= c:
            yield list(sub_set)


def bounded_subsets_sorted(s, c):
    """
    the method call the generator from itertools than
    it itarate it and every time the generator is called it return the next subset smaller than c
    the subsets are sorted by the sum of the value
    for example [50,51],[102]
    :param s: list of integers
    :param c: target number to be the bound of the subsets
    :return: generator with all the subsets smaller than c
    """
    size = 0
    sum_of_s = 0
    for i in range(len(s)):
        sum_of_s += s[i]
        size += 1
        if sum_of_s > c:
            break

    iterators_list = [None] * size
    min_element_list = [None] * size
    min_indices_list = [None] * size
    for r in range(1, size):
        iterators_list[r-1] = itertools.chain.from_iterable([sorted(itertools.combinations(s, r), key=sum)])
        min_element_list[r-1] = next(iterators_list[r-1])
    yield []
    while (any(iterators_list)):
        for it in range(len(iterators_list)):
            if iterators_list[it] is not None and iterators_list[it] is not False:
                if min_element_list[it] is None:
                    try:
                        min_element_list[it] = next(iterators_list[it])
                        if sum(min_element_list[it]) > c:
                            iterators_list[it] = False
                    except:
                        iterators_list[it] = False
        for p in range(len(min_indices_list)):
            if min_element_list[p] is None:
                min_indices_list[p] = float('inf')
            else:
                min_indices_list[p] = sum(min_element_list[p])
        index = min_indices_list.index(min(min_indices_list))
        if min_element_list[index] is not None and sum(min_element_list[index]) <= c:
            yield list(min_element_list[index])
        min_element_list[index] = None


if __name__ == '__main__':
    doctest.testmod()




