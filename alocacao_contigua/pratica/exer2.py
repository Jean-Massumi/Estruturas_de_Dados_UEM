from ed import array



class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.

    >>> p = Pilha(50)
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

    capacidade_maxima : int
    valores: array[str]
    # O índice do elemento que está no topo da pilha,
    # -1 se a pilha está vazia.
    topo: int

    def __init__(self, capacidade:int):
        '''
        Cria uma nova pilha com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''
        self.capacidade_maxima = capacidade
        self.valores = array(self.capacidade_maxima, '')
        self.topo = -1


    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Requer que a quantidade de elementos na pilha seja menor que
        capacidade_maxima.

        Exemplos
        >>> p = Pilha(50)
        >>> for i in range(50):
        ...     p.empilha(str(i))
        >>> p.empilha('a')
        Traceback (most recent call last):
        ...
        ValueError: pilha cheia
        >>> p.desempilha() == str(50 - 1)
        True
        '''
        if self.topo >= self.capacidade_maxima - 1:
            raise ValueError('pilha cheia')
        self.topo = self.topo + 1
        self.valores[self.topo] = item





    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplos
        >>> p = Pilha(50)
        >>> p.desempilha()
        Traceback (most recent call last):
        ...
        ValueError: pilha vazia
        >>> p.empilha('casa')
        >>> p.empilha('na')
        >>> p.empilha('árvore')
        >>> p.desempilha()
        'árvore'
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
        >>> p = Pilha(50)
        >>> p.vazia()
        True
        >>> p.empilha('lar')
        >>> p.vazia()
        False
        '''
        return self.topo == -1
    

    def cheia(self) -> bool:
        '''
        Devolve True se a pilha está cheia, False caso contrario.

        Eemplos:
        >>> p = Pilha(50)
        >>> p.empilha('r')
        >>> p.cheia()
        False
        >>> p.desempilha()
        'r'
        >>> for i in range(50):
        ...     p.empilha(str(i))
        >>> p.cheia()
        True
        >>> p.vazia()
        False
        '''

        return self.topo == self.capacidade_maxima - 1
    

    def capacidade(self):
        '''
        Mostra a capacidade maxima que array pode suportar.
        
        Exemplos:
        >>> p = Pilha(50)
        >>> p.capacidade()
        50
        '''

        return self.capacidade_maxima





