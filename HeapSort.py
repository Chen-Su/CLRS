def Parent(i):
    return i // 2 - 1


def Left(i):
    return 2*i + 1


def Right(i):
    return 2*i + 2


def MaxHeapify(A, i, heapsize):
    """
    Heapify the max heap
    :param A: array to store elements
    :param i: initial index
    :return:
    """
    l = Left(i)
    r = Right(i)
    largest = 0
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, heapsize)


def BuildMaxHeap(A):
    """

    :param A:
    :return:
    """
    start = len(A) // 2 - 1
    while (start >= 0):
        MaxHeapify(A, start, len(A))
        start -= 1


def HeapSort(A):
    """

    :param A:
    :return:
    """
    BuildMaxHeap(A)
    heapsize = len(A)
    while (heapsize > 1):
        A[0], A[heapsize-1] = A[heapsize-1], A[0]
        heapsize -= 1
        MaxHeapify(A, 0, heapsize)


def Insert(A, x):
    """
    把元素x插入优先队列A
    :param A:
    :param x:
    :return:
    """
    A.append(x)
    IncreaseKey(A, len(A)-1, x)


def ExtractMax(A):
    """

    :param A:
    :return:
    """
    res = A[0]
    A[0] = A[-1]
    A.pop()
    MaxHeapify(A, 0, len(A))


def IncreaseKey(A, i, x):
    """
    把A[i]增加到x
    :param A:
    :param i:
    :param x:
    :return:
    """
    A[i] = x
    while(i > 0 and A[i] > A[Parent(i)]):
        A[i] = A[Parent(i)]
        A[Parent(i)] = x
        i = Parent(i)


def Maximum(A):
    """

    :param A:
    :return:
    """
    return A[0]

A = [-1,1,2,4,3,5,0]
BuildMaxHeap(A)
print(Maximum(A))
print(A)
ExtractMax(A)
print(A)
IncreaseKey(A, 2, 10)
print(A)
Insert(A, 8)
print(A)
ExtractMax(A)
print(A)
