
from abc import ABC, abstractmethod
from typing import Any, Callable
import random


def who_start(seed = 1):
    random.seed(seed)
    return round(random.random())


def create_new_chocolate(chocolate_size=8, a=0, b=20, seed=1):
    random.seed(seed)
    res = []
    for i in range(chocolate_size):
        res.append(random.randint(a, b))
    return res


class Bins(ABC):
    """
    An abstract bins class.
    """

    def __init__(self, items=[], player_to_play=-1):
        self.num = 2
        self.valueof = lambda x: x
        if player_to_play < 0 or player_to_play > 1 :
            self.player_to_play = who_start()
        else:
            self.player_to_play = player_to_play
        if len(items) == 0:
            self.items = create_new_chocolate()
        else:
            self.items = list(items)
        self.l = 0
        self.r = len(self.items)-1

    def increase_l(self):
        self.l += 1

    def decrease_r(self):
        self.r -= 1

    def get_valueof(self,item):
        return self.items[item]

    def set_valueof(self, new_valueof: Callable):
        self.valueof = new_valueof

    def next_player(self):
        self.player_to_play = (self.player_to_play+1) % 2

    @abstractmethod
    def add_item_to_bin(self, item: float, bin_index: int):
        pass

    @abstractmethod
    def result(self):
        return None


class BinsKeepingSums(Bins):
    """
    A bins structure that keeps track only of the total sum in each bin.
    """

    def __init__(self,items, **kwargs):
        super().__init__(items, **kwargs)
        self.sums = 2*[0]

    def add_item_to_bin(self, item: float):
        self.sums[self.player_to_play] += item

    def result(self):
        return self.sums


class BinsKeepingContents(BinsKeepingSums):
    """
    A bins structure that keeps track of both the sum and the entire contents of each bin.
    """

    def __init__(self,items, **kwargs):
        super().__init__(items, **kwargs)
        self.bins = [[] for _ in range(2)]

    def add_item_to_bin(self, item: float):
        super().add_item_to_bin(item)
        self.bins[self.player_to_play].append(item)

    def result(self):
        return self.bins


if __name__ == "__main__":
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))