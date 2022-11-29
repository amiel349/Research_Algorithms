
from typing import Callable, Any
from bins import *
import outputtypes as out
import doctest


def chocolate_game(player1_algorithm: Callable, player2_algorithm: Callable, items: list = []
                  ,outputtype: out.OutputType = out.Partition, **kwargs):
    """
    In The 'Chocolate Game' there is a chocolate bar and every piece have a value
    the game is between two players and at every turn each player can choose only the left piece of the chocolate
    or the right piece
    the player with the biggest sum win
    for example: this is the chocolate: [4,3,7,5]
    first player choose the right and take 5
    second player choose also the right and take 7
    first player choose the left and take 4
    second player take the last piece 3
    second player win with 10 against 9 of first player
    >>> chocolate_game(greedy,greedy,items=[1,2,3,4],outputtype = out.Winner)
    'The winner is player number 1 with: 6 points'
    >>> chocolate_game(greedy,greedy,items=[1,2,3,4],outputtype = out.Loser)
    'The Loser is player number 2 with: 4 points'
    >>> chocolate_game(smart_algorithm, smart_algorithm, items={'a': 1, 'b':2, 'c':3, 'd':4}, outputtype=out.Partition)
    [[4, 2], [3, 1]]
    >>> chocolate_game(smart_algorithm,smart_algorithm,items=[4,3,7,5],outputtype = out.Winner)
    'The winner is player number 1 with: 11 points'
    >>> chocolate_game(greedy, smart_algorithm, items=[10, 15, 3, 5, 1], outputtype=out.Winner)
    'The winner is player number 2 with: 20 points'
    >>> chocolate_game(greedy,greedy,items=[1,2,3,4],outputtype = out.Difference)
    2
    >>> chocolate_game(greedy,greedy,items=[8, 10, 1, 4, 12, 10],outputtype = out.Partition)
    [[10, 8, 4], [12, 10, 1]]
    >>> chocolate_game(greedy, greedy, items={'a': 1, 'b':2, 'c':3, 'd':4}, outputtype=out.Winner)
    'The winner is player number 1 with: 6 points'


    """
    if isinstance(items, dict):  # items is a dict mapping an item to its value.
        item_names = items.values()
    else:
        item_names = items
    bins = outputtype.create_new_bin(item_names,**kwargs)

    while bins.l <= bins.r:
        if bins.player_to_play == 0:
            player1_algorithm(bins)
            bins.next_player()
        else:
            player2_algorithm(bins)
            bins.next_player()
    return outputtype.extract_output_from_bin(bins)


def smart_algorithm(bins: Bins):
    """
    The smart algorithm is useful the first player,
    he can calculate the sum of the even or the odd indices
    and every turn he can choose the biggest sum, the second player is 'obligated'
    to take the rest, for example if the chocolate id [1, 2, 10, 8]
    then, even is sum([1, 10]) = 11 and odd id sum([2,8])=10
    so the first player will chose 1 and if the second player choose 8 or 2 the first player
    will choose in the next turn 10 and will win
    """
    if (bins.r-bins.l) % 2 == 1:
        even = sum([bins.items[i] for i in range(bins.l, bins.r, 2)])
        odd = sum([bins.items[i] for i in range(bins.l+1, bins.r+1, 2)])

        if even > odd:
            bins.add_item_to_bin(bins.items[bins.l])
            bins.increase_l()
        else:
            bins.add_item_to_bin(bins.items[bins.r])
            bins.decrease_r()
    else:
        greedy(bins)

def greedy(bins: Bins):
    """
    The greedy algorithm always take the biggest value in the chocolate (between left and right side)
    """
    if bins.items[bins.l] > bins.items[bins.r]:
        bins.add_item_to_bin(bins.items[bins.l])
        bins.increase_l()
    else:
        bins.add_item_to_bin(bins.items[bins.r])
        bins.decrease_r()


if __name__ == '__main__':
    doctest.testmod()
