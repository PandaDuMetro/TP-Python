import numbers

maliste = [1568,"issou",12, None, 2+4j,1]


def petit(liste, nb=None):
    if (len(liste) == 0):
        return nb
    if (isinstance(liste[0], numbers.Number) is True and isinstance(liste[0], complex) is False):
        if (nb is None):
            nb = liste[0]
            liste.pop(0)
            return petit(liste, nb)
        elif (liste[0] < nb):
            nb = liste[0]
            liste.pop(0)
            return petit(liste, nb)
    liste.pop(0)
    return petit(liste, nb)


if __name__ == "__main__":
    print(petit(maliste))