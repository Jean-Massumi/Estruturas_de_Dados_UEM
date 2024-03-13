from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int 
    dir: Arvore

Arvore = No | None

def busca(arv: Arvore, val: int) -> bool:
    '''
    Devolve True se *val* está em *t*,
    False caso contrário.

    >>> t3 = No(No(None, 5, None), 7, None)
    >>> t1 = No(None, 2, No(None, 3, None))
    >>> t2 = No(No(None, -3, None), 1, t1)
    >>> t = No(t2, 4, t3)
    >>> n = No(No(No(None, -3, None), 1, No(None, 2, No(None, 3, None))), 4, No(No(None, 5, None), 7, None))

    >>> busca(None, 10)
    False
    >>> busca(t, 2)
    True
    >>> busca(t, 6)
    False
    '''
    if arv is None:
        return False
    elif val == arv.val:
        return True
    elif val < arv.val:
        return busca(arv.esq, val)
    else: # val > t.val
        return busca(arv.dir, val)
