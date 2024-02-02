from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item : int
    prox : No | None


def item(lista:list):
    '''
    Devolve um encadeamento com os mesmo itens da lista

    Exemplos
    >>> item([2,8,1,5])
    No(item=5, prox=No(item=1, prox=No(item=8, prox=No(item=2, prox=None))))
    '''

    p = No(lista[-1], None)
    q = p
    for i in range(len(lista) - 2, -1, -1):
        q.prox = No(lista[i], None)
        q = q.prox
    return p