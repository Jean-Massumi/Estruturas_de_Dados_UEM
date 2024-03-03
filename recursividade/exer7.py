def divisores(n: int, x: int) -> list:
    '''
    Devolve todos os divisores de *n* menores que *x* em uma lista.

    *n* e *x* são numeros naturais , onde x <= n 

    Exemplos:
    >>> divisores(8, 4)
    [1, 2, 4]
    >>> divisores(18, 10)
    [1, 2, 3, 6, 9]
    >>> divisores(12, 5)
    [1, 2, 3, 4]
    '''

    if x is 0:
        return []
    else:
        lista = divisores(n, x - 1)
        if n % x == 0:
            lista.append(x)

    return lista



