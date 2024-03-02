from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def muda_str(no: Lista, num: int) -> Lista:
    '''
    Devolve a mesma lista de entrada com as modificaçõs nas string, no tamanho de n
    
    Exemplos
    >>> muda_str(No('pilar', No('celular', No('céu', None))), 5)
    No(item='pilar', prox=No(item='celul', prox=No(item='céu', prox=None)))
    '''

    if no is not None:
        muda_str(no.prox, num)
        item = no.item
        if len(item) > num:
            no.item = item[:5]
        elif len(item) < num:
            no.item = item + num*''

    return no













