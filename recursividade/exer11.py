def maior_str(lst: list[str], qtd: int):
    '''
    Devolve o maior tamanho de uma string de uma lista strings

    Exemplos
    >>> maior_str(['casa', 'celular', 'ceu', 'mouse'], 4)
    7
    >>> maior_str(['computador', 'celular', 'ceu', 'mouse'], 4)
    10
    >>> maior_str(['casa', 'celular', 'ceu', 'ventilador'], 4)
    10
    >>> maior_str(['casa', 'celular', 'paralelepipedo', 'mouse'], 4)
    14
    '''

    if qtd == 1:
        return len(lst[0])
    else:
        maior = maior_str(lst, qtd - 1)
        if len(lst[qtd - 1]) > maior:
            maior = len(lst[qtd - 1])

    return maior