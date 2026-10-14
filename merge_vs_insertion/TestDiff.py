from MergeVsInsertionTimes import (insertion_sort, merge_sort)

import random
import timeit

merge_elapsed = 0.0

insertion_elapsed = 0.0

# Do the test 10 times each to get less variation
def do_test_20(lst):
    insertion_e = timeit.timeit(
        lambda: insertion_sort(lst),
        number=20
    )

    merge_e = timeit.timeit(
        lambda: merge_sort(lst),
        number=20
    )

    return insertion_e, merge_e

N = 2
while merge_elapsed >= insertion_elapsed:
    # I just realized that I multiplied the N by two when testing
    # I am not going to change that now since I already
    # submitted question 5 and the graph, so just take that into account
    # (As you can see below)
    random_list = [random.randint(1, N * 2) for i in range(N)]
    insertion_elapsed, merge_elapsed = do_test_20(random_list)
    N += 1

print("For N equal to or greater than " + str(N) + "( within 10 )")
print("Merge: ", merge_elapsed)
print("Insertion: ", insertion_elapsed)
