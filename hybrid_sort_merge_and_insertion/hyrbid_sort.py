from typing import Callable, List, TypeVar

from merge_vs_insertion.MergeVsInsertionTimes import (insertion_sort, merge)

T = TypeVar("T")  # represents generic type

def hybrid_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    n = len(data)
    if n <= 1:
        return
    elif n <= threshold:
        insertion_sort(data, comparator=comparator, descending=descending)
        return
    mid = n // 2
    left = data[0:mid]
    right = data[mid:n]
    hybrid_sort(left, threshold=threshold, comparator=comparator, descending=descending)
    hybrid_sort(right, threshold=threshold, comparator=comparator, descending=descending)
    merge(left, right, data, comparator, descending)
