"""
Define the various available output formats for a partition algorithm.
"""

from abc import ABC
from typing import Any, List
from bins import Bins, BinsKeepingContents, BinsKeepingSums


class OutputType(ABC):
    @classmethod
    def create_new_bin(cls, items, **kwargs) -> Bins:
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        pass

    @classmethod
    def extract_output_from_bin(cls, bins: Bins) -> Any:
        """
        Return the required output from the given list of filled bins.
        """
        pass


class Sums(OutputType):
    @classmethod
    def create_new_bin(cls,items, **kwargs) -> List:
        return BinsKeepingSums(items,**kwargs)

    # Output the sums of all the bins (but not the bins contents).
    @classmethod
    def extract_output_from_bin(cls, bins: Bins) -> List:
        return cls.extract_output_from_sum(bins.sums)

    @classmethod
    def extract_output_from_sum(cls, sums: List[float]) -> List:
        return sums


class Winner(Sums):
    @classmethod
    def create_new_bin(cls,items, **kwargs) -> List:
        return BinsKeepingSums(items,**kwargs)
    # Output the largest bin sum.
    @classmethod
    def extract_output_from_sum(cls, sums: List[float]) -> List:
        return f"The winner is player number {sums.index(max(sums))+1} with: {max(sums)} points"


class Loser(Sums):
    @classmethod
    def create_new_bin(cls, items, **kwargs) -> List:
        return BinsKeepingSums(items, **kwargs)
    # Output the smallest bin sum.
    @classmethod
    def extract_output_from_sum(cls, sums: List[float]) -> List:
        return f"The Loser is player number {sums.index(min(sums))+1} with: {min(sums)} points"


class Difference(Sums):
    @classmethod
    def create_new_bin(cls, items, **kwargs) -> List:
        return BinsKeepingSums(items, **kwargs)
    # Output the difference between the largest and smallest sum.
    @classmethod
    def extract_output_from_sum(cls, sums: List[float]) -> List:
        return max(sums) - min(sums)


class Partition(OutputType):
    @classmethod
    def create_new_bin(cls,items, **kwargs) -> List:
        return BinsKeepingContents(items, **kwargs)

    # Output the set of all bins.
    @classmethod
    def extract_output_from_bin(cls, bins: Bins) -> List:
        return bins.bins


class PartitionAndSums(Partition):
    @classmethod
    def create_new_bin(cls, items, **kwargs) -> List:
        return BinsKeepingContents(items, **kwargs)
    # Output the set of all bins.
    @classmethod
    def extract_output_from_bin(cls, bins: Bins) -> List:
        return bins