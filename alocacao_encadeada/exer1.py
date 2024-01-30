from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item : int
    prox : No | None


def ordem_inversa(itens:list) -> No:
    '''
    Exemplos
    >>> ordem_inversa([7, 1, 2])
    No(item=7, prox=No(item=1, prox=No(item=2, prox=None)))
    '''
    
    p = No(itens[0], None)
    q = p
    for i in range(1, len(itens)):
        q.prox = No(itens[i], None)
        q = q.prox
    return p