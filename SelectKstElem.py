import random
import QuickSort

def RandomSelect(A, left, right, k):
    """
    select k-st element in A
    :param A:
    :param left:
    :param right:
    :param k:
    :return:
    """
    if(left == right):
        return A[left]
    # line16-18 is actually random-partition()
    p = random.randrange(left, right)
    A[p], A[right] = A[right], A[p]
    pivot = QuickSort.Partition(A, left, right)
    curk = pivot  - left + 1
    if curk == k:
        return A[pivot]
    elif curk < k:
        return RandomSelect(A, pivot+1, right, k-curk)
    else:
        return RandomSelect(A, left, pivot-1, k)

A = [561, 761, 452, 512, 233, 234, 234]
for k in range(len(A)):
    print(RandomSelect(A, 0, len(A)-1, k+1))
