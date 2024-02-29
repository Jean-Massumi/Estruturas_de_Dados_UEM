from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def elem_impar(no: Lista) -> bool:
    '''
    Devolve True se há um elemento impar no encadeamento, False caso contrario.
    
    Exemplos:
    >>> elem_impar(No(2, No(5, No(8, None))))
    True
    >>> elem_impar(No(2, No(4, No(8, None))))
    False
    >>> elem_impar(No(7, No(2, No(12, None))))
    True
    >>> elem_impar(No(11, No(5, No(8, None))))
    True
    '''

    if no is None:
        return False
    else:
        return no.item % 2 == 1 or elem_impar(no.prox)