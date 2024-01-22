from ed import array

class Pilha:
    '''
    Uma coleção de strings que segue a política LIFO: o elemento mais
    recentemente inserido é o primeiro a ser removido.
    '''

    def __init__(self):
        '''
        Cria uma unica string para armazenar os elementos de uma pilha.
        '''

        self.pilha_str = ''
        
    def empilha(self, item: str):
        '''
        Adiciona o *item* na pilha.

        Exemplos:
        >>> p = Pilha()
        >>> p.vazia()
        True
        >>> p.empilha('casa')
        >>> p.vazia()
        False
        '''

        if self.pilha_str == '':
            self.pilha_str += str(item)
        else:
            self.pilha_str = ' '.join(self.pilha_str)
            self.pilha_str += f' {item}'

        self.pilha_str = self.pilha_str.split()



    def desempilha(self) -> str:
        '''
        Devolve o elemento mais recentemente adicionado da pilha.

        Requer que a pilha não esteja vazia.

        Exemplo:
        >>> p = Pilha()
        >>> p.empilha('casa')
        >>> p.empilha('fone')
        >>> p.empilha('mesa')
        >>> p.empilha('caderno')
        >>> p.desempilha()
        'caderno'
        >>> p.desempilha()
        'mesa'
        >>> p.desempilha()
        'fone'
        '''

        if self.vazia():
            raise ValueError('pilha vazia')

        item = self.pilha_str[-1]
        self.pilha_str.pop()


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
        return self.pilha_str == ''

