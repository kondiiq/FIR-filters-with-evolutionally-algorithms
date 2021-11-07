def NWD( a, b):
    """
    Funkcja zwraca NWD(największy wspólny dzielnik liczb a i b)
    :param a: Liczba naturalna
    :param b: Liczba naturalna
    :return: NWD(a, b)
    """
    if a == b:
        return a
    else:
        return NWD(b, a % b)

    