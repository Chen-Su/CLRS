def FastWay(a, t, e, x, n):
    """
    Calculate the fast way for assembly line scheduling
    :param a: a(i,j) : i装配线j装配站需要的时间
    :param t: t(i,j) : 从i装配线j装配站换线所需要的时间
    :param e: e(i) ：到达i装配线需要的时间
    :param x: x(i) ：从i装配线出来到终点需要的时间
    :param n: 每条线上装配站的数量
    :param l: 保存中间的选择结果，用于打印装配方案
    :return: 装配完成的最短时间
    """
    f = [[0 for x in range(n)] for y in range(2)]
    l = [[0 for x in range(n)] for y in range(2)]
    f[0][0] = e[0] + a[0][0]
    l[0][0] = 0
    f[1][0] = e[1] + a[1][0]
    l[1][0] = 1
    i = 1
    while(i < n):
        if(f[0][i-1] < f[1][i-1]+t[1][i-1]):
            f[0][i] = f[0][i-1] + a[0][i]
            l[0][i] = 0
        else:
            f[0][i] = f[1][i-1]+t[1][i-1] + a[0][i]
            l[0][i] = 1

        if(f[1][i-1] < f[0][i-1]+t[0][i-1]):
            f[1][i] = f[1][i-1] + a[1][i]
            l[1][i] = 1
        else:
            f[1][i] = f[0][i - 1] + t[0][i - 1] + a[1][i]
            l[1][i] = 0
        i += 1
    # print(f)
    lfinal = 0
    if(f[0][n-1] + x[0] < f[1][n-1] + x[1]):
        res = f[0][n-1] + x[0]
        lfinal = 0
    else:
        res = f[1][n-1] + x[1]
        lfinal = 1
    fastWay = []
    fastWay.append(lfinal)
    for x in range(n)[::-1]:
        fastWay.append(l[fastWay[-1]][x])
    fastWay.reverse()
    print("Fast Way:")
    for i in range(len(fastWay)):
        print('line', fastWay[i], 'station', i)
    return res

def main():
    a = [[7,9,3,4,8,4], [8,5,6,4,5,7]]
    t = [[2,3,1,3,4], [2,1,2,2,1]]
    e = [2,4]
    x = [3,2]
    n = 6
    res = FastWay(a, t, e, x, n)
    print(res)
    return

main()
