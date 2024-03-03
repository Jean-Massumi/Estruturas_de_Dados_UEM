from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    item: int
    prox: Lista

Lista = No | None

def repetir_str(str: str, n: int) -> str:
    '''
    Devolve a string repetidas *n* vezes
    
    >>> repetir_str('férias', 4)
    'fériasfériasfériasférias'
    >>> repetir_str('Motivação! ', 3)
    'Motivação! Motivação! Motivação! '
    '''

    if n is 1:
        return str
    else:
        return str + repetir_str(str, n - 1)











