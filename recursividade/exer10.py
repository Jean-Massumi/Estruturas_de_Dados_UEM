def concatene(lst: list[str], qtd: int) -> str:
    '''
    Concatena todas as strings de uma lista 

    Exemplos:
    >>> concatene(['oi ', 'tudo ', 'bem?'], 3)
    'oi tudo bem?'
    >>> concatene(['nao desista', 'por mais que', 'seja dificil!'], 3)
    'nao desistapor mais queseja dificil!'
    '''

    if qtd == 0:
        return ''
    else:
        string = concatene(lst, qtd - 1)
        string += lst[qtd - 1]

    return string