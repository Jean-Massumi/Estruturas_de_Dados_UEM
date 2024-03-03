def n_vezes(lst: list, qtd: int, n: int) -> int:
    '''
    Devolve quantas *n* vezes apareceu em uma lista.

    Exemplos:
    >>> n_vezes([1, 2, 3, 2, 4, 2, 5], 7, 2)
    3
    >>> n_vezes([1, 2, 3, 2, 4, 2, 5], 7, 8)
    0
    '''

    if qtd == 0:
        return 0
    else:
        repeticao = n_vezes(lst, qtd - 1, n)
        if n == lst[qtd - 1]:
            repeticao += 1

    return repeticao


