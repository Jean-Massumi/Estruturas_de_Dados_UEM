from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int 
    dir: Arvore

Arvore = No | None

def num_folhas(arv: Arvore) -> No:
    '''
    Determina a quantidade de folhas em 't'.
    Uma folha é um nó sem nenhum filho

    Exemplos
    >>> t1 = No(None, 7, No(None, 1, None))
    >>> t1
    No(esq=None, val=7, dir=No(esq=None, val=1, dir=None))
    >>> t2 = No(No(None, 4, None), 8, t1)
    >>> t3 = No(No(None, 5, None), 6, None)
    >>> t4 = No(t2, 4, t3)

    >>> num_folhas(t2)
    2
    >>> num_folhas(t3)
    1
    >>> num_folhas(t4)
    3
    '''

    if arv is None:
        return 0 
    else:
        if arv.esq is None and arv.dir is None:
            return 1
        else:
            return num_folhas(arv.esq) + num_folhas(arv.dir)
        
