import  queue

def HuffMan(C, f):
    """

    :param c:
    :return:
    """
    n = len(C)
    Q = queue.PriorityQueue()
    for x in range(n):
        Q.put((f[x], C[x]))

    for i in range(n-1):
        left = Q.get()
        right = Q.get()
        newNode = (left[0]+right[0], left[1]+right[1])
        print(newNode)
        Q.put(newNode)

    return Q.get()

def main():
    C = 'fecbda'
    f = [5, 9, 12, 13, 16, 45]

    HuffMan(C, f)


main()

