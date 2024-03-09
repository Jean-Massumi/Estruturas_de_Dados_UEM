def valor_contido(lst: list[int], n: int) -> bool:
    '''
    Devolve True se *n* está na lista, False caso contrario.

    A lista deve está ordenada para usar a busca binaria.

    >>> valor_contido([1, 3, 5, 6, 9, 11], 5)
    True
    >>> valor_contido([1, 3, 5, 6, 9, 11, 21], 21)
    True
    >>> valor_contido([1, 3, 5, 6, 9, 11], 30)
    False
    '''

    def busca_binaria(lst: list[int], n: int, inicio: int, fim: int) -> bool:
        
        if inicio > fim:
            return False
        else:
            m = (inicio + fim)//2
            if n == lst[m]:
                return True
            elif n < lst[m]:
                return busca_binaria(lst, n, inicio, m - 1)
            elif n > lst[m]:
                return busca_binaria(lst, n, m + 1, fim)
        
    return busca_binaria(lst, n, 0, len(lst) - 1)


      

    





    