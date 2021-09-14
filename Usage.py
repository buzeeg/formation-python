usage: str = """Super commande - Copyright Symbio - 2021
  -o: image...
  -h: aide
  -? fesffse
fesfsefsef
fesf"""


# Utiliser les docstrings pour la doc avec PyDoc et  tester les exemples avec DocTest
def fonction(a, b):
    """
    La fonction fonction est une fonction qui prend en argument :
    :param a: int
    :param b: int
    :return: a + b

    Examples:
        >>> first = 5
        >>> second = 8
        >>> fonction(first, second)
        13
        >>> fonction(5, 6)
        11
        >>> fonction(12, 6)
        11
        >>>
    """
    return a+b


if __name__ == '__main__':
    # Display multiline comment
    print(usage)

    # Use PyDoc to extract help from docstrings
    help(fonction)

    # Separators
    import os
    print(os.sep)
    print(os.linesep)
    print(os.altsep)
    print(os.extsep)
    print(os.pathsep)
    print(fonction(2, 3))

    # Tests
    print("Testing...")
    import doctest
    doctest.testmod()
