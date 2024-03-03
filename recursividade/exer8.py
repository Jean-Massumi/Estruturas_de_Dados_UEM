def exponecial(a: int, n: int) -> int:
    '''
    Calcula o a**n
    
    Exemplos
    >>> exponecial(2, 4)
    16
    >>> exponecial(3, 4)
    81
    >>> exponecial(2, 7)
    128
    '''

    if n is 0:
        return 1 
    else:
        return a * exponecial(a, n - 1)

print(exponecial(3, 4))