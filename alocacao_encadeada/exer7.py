from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: No | None

def maior_elem(n: No | None):
    '''
    Encontra o valor maior entre todos os itens do encadeamento
    
    Exemplos:
    >>> n = No(32, No(77, No(11, None)))
    >>> maior_elem(n)
    77
    '''

    maior = 0    
    if n is None:
        return 0
    else:
        q = n
        maior = q.item
        while q.prox is not None:
            q = q.prox
            if q.item > maior:
                maior = q.item
            
    return maior