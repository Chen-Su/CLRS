def QuickSort(A, left, right):
    """

    :param A:
    :param left:
    :param right:
    :return:
    """
    if(left >= right):
        return
    pivot = Partition(A, left, right)
    QuickSort(A, left, pivot-1)
    QuickSort(A, pivot+1, right)


def Partition(A, left, right):
    """

    :param A:
    :param left:
    :param right:
    :return:
    """
    x = A[right]
    i, j = left, right
    index = left
    while(index < right):
        if(A[index] <= x):
            A[index], A[i] = A[i], A[index]
            i += 1
        index += 1
    A[i], A[right] = A[right], A[i]
    return i

A = [1,3,5,6,2]
QuickSort(A, 0, len(A)-1)
print(A)

