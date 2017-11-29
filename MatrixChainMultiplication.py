import  sys

def MatrixChainOrder(p):
    """
    Calculate optimal order for matrix chain multiplication
    :param p: Matrix[i]'dimension is p[i]*p[i+1]
    :return: minimum calculate times
    """
    n = len(p) - 1
    m = [[sys.maxsize for x in range(n)] for x in range(n)]
    for x in range(n):
        m[x][x] = 0
    s = [[0 for x in range(n)] for x in range(n)]
    l = 2
    while(l <= n):  # l <- 2 : n
        i = 0
        while(i <= n-l):    # i <- 1 : n-l
            j = i+l-1
            k = i
            while(k<j):    # k <- i : j-1
                # A(i...k) * A(k+1...j)
                tmp = p[i]*p[k+1]*p[j+1] + m[i][k] + m[k+1][j]
                if tmp < m[i][j]:
                    m[i][j] = tmp
                    s[i][j] = k
                k += 1
            i += 1
        l += 1
    # for x in range(n):
    #     print(m[x])
    # for x in range(n):
    #     print(s[x])
    # Print Solution:
    PrintOptimalPattern(s, 0, n-1)
    print()
    return m[0][n-1]


def PrintOptimalPattern(s, i, j):
    """
    Print pattern recursively
    :param s:
    :param i:
    :param j:
    :return:
    """
    if i == j:
        print('A', end='')
    else:
        print('(', end='')
        PrintOptimalPattern(s, i, s[i][j])
        PrintOptimalPattern(s, s[i][j]+1, j)
        print(')', end='')


def main():
    p = [30, 35, 15, 5, 10, 20, 25]
    print(MatrixChainOrder(p))


main()
