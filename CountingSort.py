def CountingSort(A, B, k):
    """

    :param A: Input list
    :param B: result list
    :param k: max(A) <= k
    :return:
    """
    C = []
    for i in range(k+1):
        C.append(0)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(k+1):
        if i > 0:
            C[i] = C[i] + C[i-1]
    for i in range(len(A)):
        j = len(A) - i - 1
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1
    return

A = [5, 4, 2, 1, 3, 1, 0]
B = [0 for i in range(len(A))]
CountingSort(A, B, 10)
print(B)