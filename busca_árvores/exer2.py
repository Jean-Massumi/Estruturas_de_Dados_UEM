def busca_binaria(lst: list[int], val: int) -> bool:
    '''
    Devolve True se o *valor* estiver na lista, False caso contraio.
    O arranjo deve está ordenado de forma nao decrescente.
    
    Exemplos
    >>> busca_binaria([1, 3, 5, 6, 9, 11], 5)
    True
    >>> busca_binaria([1, 3, 5, 6, 9, 11, 21], 21)
    True
    >>> busca_binaria([1, 3, 5, 6, 9, 11], 30)
    False
    '''
    inicio , fim = 0, len(lst) - 1

    while inicio <= fim:
        meio = (inicio + fim)// 2
        if val < lst[meio]:
            fim = meio - 1
        elif val > lst[meio]:
            inicio = meio + 1
        else:
            return True

    return False


