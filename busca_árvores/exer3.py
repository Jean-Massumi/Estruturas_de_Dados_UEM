import time


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

t_inicio = time.time()
busca_binaria(list(range(0,10000000)), 5)
t_fim = time.time()
print(t_inicio - t_fim)


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

    def _busca_binaria(lst: list[int], n: int, inicio: int, fim: int) -> bool:
        
        if inicio > fim:
            return False
        else:
            m = (inicio + fim)//2
            if n == lst[m]:
                return True
            elif n < lst[m]:
                return _busca_binaria(lst, n, inicio, m - 1)
            elif n > lst[m]:
                return _busca_binaria(lst, n, m + 1, fim)
        
    return _busca_binaria(lst, n, 0, len(lst) - 1)

t2_inicio = time.time()
valor_contido(list(range(0,10000000)), 5)
t2_fim = time.time()
print(t2_inicio - t2_fim)


# Ao fazer o experimento do tempo de execução dos dois códigos acima, nota-se que a funçao de 
# recursividade teve um tempo menor que a função interativa.

