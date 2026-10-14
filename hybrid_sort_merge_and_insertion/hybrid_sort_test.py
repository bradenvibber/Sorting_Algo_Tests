from hyrbid_sort import hybrid_sort

import random
import timeit

hybrid_elapsed = 0.0

def do_test_20(lst, n_cross):
    hybrid_e = timeit.timeit(
        lambda: hybrid_sort(lst, threshold=n_cross, ),
        number=20
    )

    return hybrid_e


N, n_cross = 0, 0
while N != -1 and n_cross != -1:
    print("Testing Hybrid Sort (enter -1 for insertion cross N to stop)")
    N = int(input("Enter the number of values in the list: "))
    n_cross = int(input("Enter the N at which you want insertion sort to be used: "))

    random_list = [random.randint(1, N) for i in range(N)]

    time = do_test_20(random_list, n_cross)

    print("The time taken to sort: ", time)
