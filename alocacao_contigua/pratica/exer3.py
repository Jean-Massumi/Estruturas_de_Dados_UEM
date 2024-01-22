from ed import array

CAPACIDADE = 100


class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha()
    >>> p.vazia()
    True
    >>> p.empilha('O')
    >>> p.empilha('que')
    >>> p.empilha('escrever?')
    >>> p.vazia()
    False
    >>> p.desempilha()
    'escrever?'
    >>> p.empilha('fazer')
    >>> p.empilha('agora?')
    >>> while not p.vazia():
    ...     p.desempilha()
    'agora?'
    'fazer'
    'que'
    'O'
    '''

    valores: array[str]
    # O índice do elemento que está no topo da pilha,
    # -1 se a pilha está vazia.
    topo: int

    def __init__(self):
        '''
        Cria uma nova pilha com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''

        self.valores = array(CAPACIDADE, '')
        self.topo = -1


    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> p = Pilha()
        >>> for i in range(CAPACIDADE):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.desempilha() == str(CAPACIDADE - 1)
        True
        '''

        if self.topo >= CAPACIDADE - 1:
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores[self.topo] = item


    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha()
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'

        >>> p = Pilha()
        >>> p.empilha('um')
        >>> p.empilha('carro')
        >>> p.empilha('mouse')
        >>> p.empilha('computador')
        >>> p.empilha('UEM')
        >>> inverte_pilha(p)
        >>> p.desempilha()
        'um'
        >>> p.desempilha()
        'carro'
        >>> p.desempilha()
        'mouse'
        >>> p.desempilha()
        'computador'
        >>> p.desempilha()
        'UEM'
        '''

        if self.vazia():
            raise ValueError('pilha vazia')
        item = self.valores[self.topo]
        self.topo = self.topo - 1
        return item


    def vazia(self) -> bool:
        '''
        Devolve True se a pilha está vazia, False caso contrário.

        Exemplos
        >>> p = Pilha()
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1


def inverte_pilha(p:Pilha):
    '''
    Inverte a ordem dos elementos de uma pilha.
    '''

    for i in range(p.topo, p.topo//2, -1):
        guardar = p.valores[p.topo - i]
        p.valores[p.topo - i ] = p.valores[i]
        p.valores[i] = guardar


