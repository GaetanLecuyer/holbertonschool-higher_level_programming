#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Ajoute deux entiers.

    Args:
        a (int or float): Le premier nombre.
        b (int or float): Le deuxieme nombre. Par defaut : 98.

    Returns:
        int: La somme de a et b.

    Raises:
        TypeError: Si a ou b n'est pas un entier ou un flottant.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a doit etre un entier ou b doit etre un entier")

    a = int(a)
    b = int(b)

    return a + b


# Test fonctionnel
result = add_integer(3, 5)
expected = 8
assert result == expected, f"Erreur : resultat obtenu = {result}, resultat attendu = {expected}"
