from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None

def copia(n: No | None) -> No | None:
    '''
    Devolve o início de um outro encadeamento que é uma cópia do encadeamento de entrada.
    
    Exemplos
    >>> p = No(10, No(20, No(30, None)))
    >>> q = copia(p)
    >>> # quanto mudamos p,
    >>> # q não é alterado pois é uma cópia
    >>> p.item = 1
    >>> p.prox.item = 2
    >>> p.prox.prox.item = 3
    >>> p
    No(item=1, prox=No(item=2, prox=No(item=3, prox=None)))
    >>> q
    No(item=10, prox=No(item=20, prox=No(item=30, prox=None)))

    >>> copia(None)
    '''


    if n is None:
        return None
    else:
        p = n
        copia_no = No(p.item, None)
        q = copia_no
        while p.prox is not None:
            p = p.prox
            q.prox = No(p.item, None)
            q = q.prox
        
    return copia_no
