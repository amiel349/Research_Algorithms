import numpy as np
import networkx as nx
from networkx import incidence_matrix
from scipy.optimize import linprog


def maximum_weight_fractional_matching(G: nx.Graph, weight="weight", **linprog_options):
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
        c, A_ub=A, b_ub=b, bounds=bounds, method="highs", options=linprog_options)
    return dict(zip(G.edges, np.abs(np.round(res.x, 3))))