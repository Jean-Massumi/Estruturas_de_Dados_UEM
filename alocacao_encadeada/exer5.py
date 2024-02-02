from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item:int
    prox: No | None



def soma(p: No | None) -> int:
    '''
    Devolve a soma dos itens do No.

    Exemplos
    >>> soma(None)
    0
    >>> soma(No(10, None))
    10
    >>> soma(No(20, No(10, None)))
    30
    >>> soma(No(4, No(20, No(10, None))))
    34
    '''

    soma = 0
    
    if p is None:
        return 0
    else:
        q = p
        soma += q.item
        while q.prox is not None:
            q = q.prox
            soma += q.item
            
    return soma