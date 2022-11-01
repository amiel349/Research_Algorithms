import doctest
graph = {
    "a": ["b", "c"],  # a-----------b
    "b": ["a", "d"],  # |           |
    "c": ["a", "d"],  # |           |
    "d": ["e"],       # c-----------d-----------e
    "e": ["d"]
}


def four_neighbor_function(node) -> list:
    (x, y) = node
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def alphabet_neighbor_function(node) -> list:
    return [chr(ord(node) + 1), chr(ord(node) - 1)]


def graph_neighbor_function(node) -> list:
    if node in graph.keys():
        return graph[node]


def breadth_first_search(start, end, neighbor_function):
    """
    Generic function of BFS, given a start node, end node and a neighbors function
    the function print if there is a path between the node or no

    :param start: the node from where we begin the BDS
    :param end: the node we are trying to reach
    :param neighbor_function: a function the return a list with the neighbors of the given node
    :return: the function return a str of the path if it exists or empty string if it doesnt exists

    >>> breadth_first_search((0, 0), (2, 2), four_neighbor_function)
    '(0, 0) -> (1, 0) -> (2, 0) -> (2, 1) -> (2, 2)'
    >>> breadth_first_search('a', 'e', alphabet_neighbor_function)
    'a -> b -> c -> d -> e'
    """
    queue = []
    visited = []
    path = {}
    queue.append(start)
    visited.append(start)
    path[start] = start
    flag = False
    while queue:
        if flag:
            break
        node = queue.pop(0)
        for i in neighbor_function(node):
            if i not in visited:
                queue.append(i)
                visited.append(i)
                path[i] = node
            if node == end:
                flag = True
                break

    if end not in path:
        return f"There is no path between '{start}' and '{end}'"
    node = end
    path_to_print = []
    path_to_print.append(end)
    while node != start:
        node = path[node]
        path_to_print.append(node)
    ans = ""
    for i in range(len(path_to_print) - 1, -1, -1):
        ans += f"{path_to_print[i]} -> "
    return ans[0:-4]


if __name__ == '__main__':
    doctest.testmod()

