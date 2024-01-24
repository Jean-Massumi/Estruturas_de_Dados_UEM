from ed import array

class Fila:
    '''
    Uma coleção de strings que segue a política FIFO: o primeiro a ser inserido
    é o primeiro a ser removido.

    Exemplos
    >>> f = Fila(50)
    >>> f.vazia()
    True
    >>> f.enfileira('Amanda')
    >>> f.enfileira('Fernando')
    >>> f.enfileira('Márcia')
    >>> f.vazia()
    False
    >>> f.desenfileira()
    'Amanda'
    >>> f.enfileira('Pedro')
    >>> f.enfileira('Alberto')
    >>> while not f.vazia():
    ...     f.desenfileira()
    'Fernando'
    'Márcia'
    'Pedro'
    'Alberto'
    '''

    valores: array[str]
    # Indíce do último elemento da fila.
    fim: int
    # Indíce do primeiro elemento da fila.
    inicio: int

    # O início é incrementado em desenfileira e o fim é incrementado em enfileira.
    # A fila está vazia se fim < inicio.

    def __init__(self, CAPACIDADE:int):
        '''
        Cria uma nova fila com capacidade para armazenar *CAPACIDADE*
        elementos.
        '''

        self.CAPACIDADE = CAPACIDADE
        self.valores = array(self.CAPACIDADE, '')
        self.inicio = 0
        self.fim = -1

    def enfileira(self, item: str):
        '''
        Adiciona *item* no final da fila.

        Requer que a quantidade de elementos na fila seja menor que
        *CAPACIDADE*.

        Exemplos
        >>> f = Fila(50)
        >>> for i in range(f.CAPACIDADE):
        ...     f.enfileira(str(i))
        >>> f.enfileira('a')
        Traceback (most recent call last):
        ...
        ValueError: fila cheia
        >>> f.desenfileira()
        '0'
        >>> f.desenfileira()
        '1'
        '''
        if self.fim >= self.CAPACIDADE - 1:
            raise ValueError('fila cheia')
        self.fim += 1
        self.valores[self.fim] = item

    def desenfileira(self) -> str:
        '''
        Remove e devolve o primeiro elemento da fila.

        Requer que a fila não esteja vazia.

        Exemplos
        >>> f = Fila(50)
        >>> f.desenfileira()
        Traceback (most recent call last):
        ...
        ValueError: fila vazia
        >>> f.enfileira('Márcia')
        >>> f.enfileira('João')
        >>> f.enfileira('Pedro')
        >>> f.desenfileira()
        'Márcia'
        '''
        if self.vazia():
            raise ValueError('fila vazia')
        item = self.valores[self.inicio]
        self.inicio += 1
        return item

    def vazia(self) -> bool:
        '''
        Devolve True se a fila está vazia, False caso contrário.

        Exemplos
        >>> f = Fila(50)
        >>> f.vazia()
        True
        >>> f.enfileira('Jorge')
        >>> f.vazia()
        False
        '''
        return self.fim < self.inicio



    def capacidade(self):
        '''
        Devolve o tamanho da capacidade de uma fila.
        '''

        return self.CAPACIDADE