from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int 
    dir: Arvore

Arvore = No | None

def valores_nivel(arv: Arvore, n: int) -> list[int]:
    '''
    Devolve os nós que estão no nível *n* de *t*.

    Exemplos
    >>> t1 = No(None, 7, No(None, 1, None))
    >>> t1
    No(esq=None, val=7, dir=No(esq=None, val=1, dir=None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(No(None, 5, None), 6, None)
    >>> t4 = No(t2, 4, t3)

    >>> valores_nivel(None, 0)
    []
    >>> valores_nivel(t4, 0)
    [4]
    >>> valores_nivel(t4, 2)
    [4, 7, 5]
    >>> valores_nivel(t4, 3)
    [1]
    '''

    if arv is None:
        return []
    else:
        if n == 0:
            return [arv.val]
        else:
            return valores_nivel(arv.esq, n - 1) + valores_nivel(arv.dir, n - 1)


