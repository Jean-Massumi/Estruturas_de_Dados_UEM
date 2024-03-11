from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

Arvore = No | None

def qtd_ele(arv: Arvore) -> int:
    '''
    Devolve a quantidade de elementos de uma arvore

    Exemplos:
    >>> qtd_ele(No(No(None, 2, None), 6, No(None, 11, None)))
    3
    >>> t3 = No(None,31,None)
    >>> t2 = No(None,11,None)
    >>> t1 = No(None,13,t3)
    >>> a = No(t1,20,t2)
    >>> qtd_ele(a)
    4
    '''

    if arv is None:
        return 0
    else:
        return 1 + qtd_ele(arv.esq) + qtd_ele(arv.dir)


