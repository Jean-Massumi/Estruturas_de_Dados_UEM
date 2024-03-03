from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def produto(n: int) -> int:
    '''
    Calcula o produto dos numeros até n.

    1, 2, 3, ..., n

    Exemplos
    >>> produto(5)
    120
    >>> produto(1)
    1
    >>> produto(10)
    3628800
    '''

    if n is 0:
        return 1
    else:
        return n * produto(n - 1)
