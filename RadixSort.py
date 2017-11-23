import CountingSort

def newCountingSort(A, d):
    """
    sort A on digit i stably
    :param A:
    :param d:
    :param k: omitted because k = 10
    :return:
    """
    B = [0 for i in range(len(A))]
    C = [0 for i in range(10)]
    for i in range(len(A)):
        C[A[i]//(10**(d-1))%10] += 1    # get number in digit i
    for i in range(len(C)):
        if i > 0:
            C[i] = C[i] + C[i-1]
    for i in range(len(A)):
        B[C[A[i]//(10**(d-1))%10]-1] = A[i]
        C[A[i] // (10 ** (d - 1)) % 10] -= 1
    return B


def RadixSort(A, d):
    """
    :param A: value list
    :param d: any value in A have d digits
    :return:
    """
    for i in range(d):
        # do use a stable sort to sort array A on digit i
        A = newCountingSort(A, i+1)
        # print(A)
    return A

A = [512, 234, 452, 761, 233, 561, 234]
A = RadixSort(A, 3)
print(A)