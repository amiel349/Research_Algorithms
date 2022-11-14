import doctest


class List(list):
    """
    >>> mylist[0, 1, 3]
    66
    >>> mylist[0]
    [[1, 2, 3, 33], [4, 5, 6, 66]]
    >>> mylist[0, 1, 3] = 55
    >>> mylist[0, 1, 3]
    55
    >>> mylist[0, 0] = [0, 0, 0, 0]
    >>> mylist[0, 0]
    [0, 0, 0, 0]
    >>> my_big_list[0, 0, 0, 1]
    2
    >>> my_big_list[0]
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
    >>> my_big_list[0, 0, 0] = [-1, -1, -1]
    >>> my_big_list[0, 0, 0]
    [-1, -1, -1]



    """
    def __getitem__(self, keys):
        if isinstance(keys, int):
            return super(List, self).__getitem__(keys)
        ans = self
        for i in keys:
            ans = ans[i]
        return ans

    def __setitem__(self, key, value):
        if isinstance(key, int):
            return super().__setitem__(key, value)
        ans = self
        size = len(key)-1
        for i in range(size):
            ans = ans[key[i]]
        ans[key[len(key)-1]] = value
        return self


if __name__ == '__main__':
    mylist = List([
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    ]
    )
    my_big_list = List([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
                        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
                        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
                        [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]])
    doctest.testmod()
