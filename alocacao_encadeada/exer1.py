from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    '''
    Cria o mesmo encadeamento na ordem: primeiro o nó com o 7, depois o nó com o 1 e depois o nó com o 2.

    Exemplos
    >>> n = No(7, None)
    >>> n
    No(item=7, prox=None)
    >>> q = n
    >>> while q.prox is not None:
    ...     q = q.prox
    >>> q.prox = No(1, None)
    >>> n
    No(item=7, prox=No(item=1, prox=None))
    >>> while q.prox is not None:
    ...     q = q.prox
    >>> q.prox = No(2, None)
    >>> n
    No(item=7, prox=No(item=1, prox=No(item=2, prox=None)))
    '''

    item : int
    prox : No | None