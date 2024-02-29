from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def elem_positivo(no: Lista) -> Lista:
    '''
    Devolve uma nova lista encadeada com os elementos positivos da lista de entrada

    Exemplos
    >>> elem_positivo(No(2, No(-3, No(8, No(-10, None)))))
    No(item=2, prox=No(item=8, prox=None))
    >>> elem_positivo(No(-9, No(2, No(8, No(-10, None)))))
    No(item=2, prox=No(item=8, prox=None))
    >>> elem_positivo(No(-11, No(4, No(-8, No(16, None)))))
    No(item=4, prox=No(item=16, prox=None))
    >>> elem_positivo(No(3, No(-4, No(-8, No(16, No(20, None))))))
    No(item=3, prox=No(item=16, prox=No(item=20, prox=None)))
    '''

    if no is None:
        return None
    else:
        nova_lista = elem_positivo(no.prox)
        if no.item > 0:
            nova_lista = No(no.item, nova_lista)

    return nova_lista

print(elem_positivo(No(-11, No(4, No(-8, No(16, None))))))