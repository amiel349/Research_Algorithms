import numpy as np
from scipy.optimize import linprog
import random
import networkx as nx
from networkx import incidence_matrix
import matplotlib.pyplot as plt


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{ orig_func.__name__} with optimization method = '{kwargs['method']}' "
              f"and G(V={len(args[0].nodes)},E={len(args[0].edges)})ran in: {t2} sec")
        return result, t2
    return wrapper


@my_timer
def maximum_weight_fractional_matching(G: nx.Graph, method="highs", weight="weight", **linprog_options):
    """
    documentation for this method can be view at:
    https://github.com/OLAnetworkx/networkx/blob/max-weight-frac-match/networkx/algorithms/maximum_weight_fractional_matching.py
    :param G: networkX undirected graph
    :param method: method for linprog optimization highs_ds or highs_ipm
    :param weight: attribute to be weight of the edges
    :param linprog_options: linprog options
    :return:
    """

    if G.number_of_nodes() == 0 or G.number_of_edges() == 0:
        return dict()
    c = [G.edges[edge].get(weight, 1) for edge in G.edges]
    b = [1] * len(G.nodes)
    bounds = (-1, 0)
    A = -incidence_matrix(G)
    res = linprog(
        c, A_ub=A, b_ub=b, bounds=bounds, method=method, options=linprog_options)
    return dict(zip(G.edges, np.abs(np.round(res.x, 3))))


def run(num_of_nodes: list):
    """
     calculate the time of maximum_weight_fractional_matching with the different method highs(highs_ds vs highs_ipm)
     for linprog method
    :param num_of_nodes: list with number of nodes for the graphs used in maximum_weight_fractional_matching
    """
    highs_ds = []
    highs_ipm = []
    n_p = []
    for n in num_of_nodes:
        p = random.uniform(0.1, 1)
        G = nx.gnp_random_graph(n, p)
        n_p.append(f'G({len(G.nodes)},{len(G.edges)})\np={p:.1f}')
        highs_ds.append(maximum_weight_fractional_matching(G, method='highs-ds')[1])
        highs_ipm.append(maximum_weight_fractional_matching(G, method='highs-ipm')[1])

    plot_ds_vs_ipm(highs_ds, highs_ipm, num_of_nodes, n_p)


def plot_ds_vs_ipm(ds: list, ipm: list, nodes: list, n_p: list):
    """
    plot the functions (num of nodes/time) of highs_ds and highs_ipm from the optimization method in linporg used in function
    maximum_weight_fractional_matching
    :param ds: list with the time in seconds for Maximum Weight Fractional Matching using high_ds optimization
    :param ipm: list with the time in seconds for Maximum Weight Fractional Matching using high_ds optimization
    :param nodes: list with the number of nodes
    :param n_p: list with the number of nodes and probability of edge between every 2 nodes for x-label
    """
    x_axis = np.arange(len(nodes))
    plt.plot(x_axis, ipm, label=f'highs_ipm optimization')
    plt.plot(x_axis, ds, label=f'highs_ds optimization')
    plt.xticks(x_axis, n_p)
    plt.legend()
    plt.ylabel('Time (seconds)')
    plt.xlabel('Number of nodes in the graph\nG(V,E)\nP=probability')
    plt.title('Maximum Weight Fractional Matching Optimization - highs_ipm VS Highs_ds')
    plt.show()


if __name__ == '__main__':

    run([20, 100, 200, 400, 600, 800, 1000, 1500, 2000])
