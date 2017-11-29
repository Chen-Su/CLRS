def LCSLength(x, y):
    """
    Calculate the longest common subsequence length of x and y
    :param x:
    :param y:
    :return: length
    """
    m, n = len(x), len(y)
    c = [[0 for y in range(n+1)] for x in range(m+1)]
    b = [[0 for y in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                c[i][j] = 0
                b[i][j] = ''
            elif x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = u'\u2196' # left-up arrow
            else:
                if c[i][j-1] > c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    b[i][j] = u'\u2190' # left arrow
                else:
                    c[i][j] = c[i-1][j]
                    b[i][j] = u'\u2191'  # up arrow
    # for i in range(m):
    #     print(c[i])
    # for i in range(len(b)):
    #     print(b[i])
    PrintLCS(b, x, m, n)
    print()
    return c[m][n]

def PrintLCS(b, x, i, j):
    """
    Print one of LCS in x and y(not need in Print())
    :param b: data structure stored LCS information
    :param x: sequence x
    :param i: subindex
    :param j: subindex
    :return:
    """
    if i == 0 or j == 0:
        return
    if b[i][j] == u'\u2196':    # left-up arrow
        PrintLCS(b, x, i-1, j-1)
        print(x[i-1], end=' ')
    elif b[i][j] == u'\u2190':  # left arrow
        PrintLCS(b, x, i, j-1)
    else:
        PrintLCS(b, x, i-1, j)


def main():
    x = ['A','B','C','B','D','A','B']
    y = ['B','D','C','A','B','A']
    s1 = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
    s2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
    LCSLength(x,y)
    LCSLength(s1, s2)


main()