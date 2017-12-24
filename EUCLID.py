def Euclid(a, b):
    """

    :param a:
    :param b:
    :return: greatest common divisor
    """
    if b == 0:
        return a

    return Euclid(b, a % b)

print(Euclid(41, 2))