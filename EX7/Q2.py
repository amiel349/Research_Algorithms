import networkx as nx
from networkx import approximation as approx
import math
import doctest
import itertools
import matplotlib.pyplot as plt
"""
The Theoretical bound for the approximation algorithm is O(|V|/(log|V|)^2) 
this is a maximization problem means that 
the optimal solution is bigger than the approximation
so the ratio is calculated - optimal/approximation

Explanation about approximation algorithms
https://www.youtube.com/watch?v=41MC-q5--Fk
"""
empiric_results = []
theoretic_results = []


def approx_vs_optimal_max_clique_algorithm(n_lst: list, p_lst: list):
    """
    Method that compare algorithms of maximal clique- approximation vs exponential
    :param n_lst: list on number of vertices
    :param p_lst: list of probabilities
    note: n_lst and p_lst should be of the same size and even
    """
    for p in p_lst:
        empiric_lst = []
        theoretic_lst = []
        for n in n_lst:
            G = nx.gnp_random_graph(n, p)
            max_clique_approx = len(approx.max_clique(G))  # biggest clique using approx algorithm
            max_clique_exp = max([len(i) for i in list(nx.find_cliques(G))])  # biggest clique using exponential algorithm
            empiric_ratio = max_clique_exp/max_clique_approx
            theoretic_ratio = n/(math.log(n)**2)
            empiric_lst.append(empiric_ratio)
            theoretic_lst.append(theoretic_ratio)
        empiric_results.append(empiric_lst)
        theoretic_results.append(theoretic_lst)
    approx_vs_optimal_plot(n_lst, p_lst)


def approx_vs_optimal_plot(n_lst: list, p_lst: list):
    """
    Method that plot the ratio between the clique approximation algorithm and
    an optimal solution as a function of n*p
    :param n_lst: list on number of vertices
    :param p_lst: list of probabilities
    """
    size = int(len(p_lst)/2)
    fig, axs = plt.subplots(nrows=2, ncols=size, sharex='all')
    i = 0
    for ax in axs.flat:
        ax.plot(n_lst, empiric_results[i], label=f'Approximation results ratio')
        ax.plot(n_lst, theoretic_results[i], label=f'Theoretical results ratio (Upper bound)')
        ax.legend()
        ax.set(xlabel='number of vertices', ylabel='Ratio', title=f'P = {p_lst[i]}')
        i += 1

    fig.suptitle('Max clique  - approx VS Theoretical')
    plt.show()


if __name__ == '__main__':
    p = [0.2, 0.3, 0.4, 0.5, 0.7, 0.8]
    n = [10, 20, 40, 60, 80, 100]
    approx_vs_optimal_max_clique_algorithm(n, p)


