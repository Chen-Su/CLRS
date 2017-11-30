import sys

def ActivitySelectDP(s, f):
    """
    Activity selection by dynamic programming
    :param s: s[i] : a[i]'s start time
    :param f: f[i] : a[i]'s finish time
    :return:
    """
    s = [0] + s + [sys.maxsize]
    f = [0] + f + [sys.maxsize]
    n = len(s)
    c = [[0 for x in range(n)] for x in range(n)]
    b = [[0 for x in range(n)] for x in range(n)]
    l = 3
    while(l <= n):
        for i in range(n-l+1):
            j = i+l-1
            k = i+1
            while(k < j):
                if(s[k] >= f[i] and f[k] <= s[j]):
                    if(c[i][j] < c[i][k] + c[k][j] + 1):
                        c[i][j] = c[i][k]+c[k][j]+1
                        b[i][j] = k
                k += 1
        l += 1
    # for x in range(n):
    #     print(c[x])
    PrintSolution(b, 0, n-1)
    return c[0][n-1]


def PrintSolution(s, i, j):
    """
    :param s:
    :param i:
    :param j:
    :return:
    """
    k = s[i][j]
    if i < k and k < j:
        PrintSolution(s, i, k)
        print(k, end=' ')
        PrintSolution(s, k, j)
    return


def ActivitySelectGreedy(s, f):
    res = []
    n = len(s)
    for i in range(n):
        if i == 0 or s[i] >= f[res[-1]]:
            res.append(i)
    print(res)
    return len(res)


def main():
    s = [1,3,0,5,3,5,6,8,8,2,12]
    f = [4,5,6,7,8,9,10,11,12,13,14]

    print(ActivitySelectDP(s,f))
    print(ActivitySelectGreedy(s,f))

main()