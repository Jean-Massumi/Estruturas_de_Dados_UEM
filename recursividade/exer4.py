from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def valor_maximo(no: Lista) -> int | None:
    '''
    Devolve o maior valor de uma lista encadeada, caso a lista for vazia, devolve None

    Exemplos:
    >>> valor_maximo(No(3, No(-4, No(20, No(16, No(7, None))))))
    20
    >>> valor_maximo(None) is None
    True
    '''

    if no is None:
        return None
    else:
        m = valor_maximo(no.prox)
        if m is None:
            m = no.item
        elif no.item > m:
            m = no.item
    return m

print(valor_maximo(No(3, No(-4, No(20, No(16, No(7, None)))))))