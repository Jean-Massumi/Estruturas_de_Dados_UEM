from __future__ import annotations
from ed import array

class Colecao:
    '''
    Uma Coleção de figurinhas que permite gerenciar
    o álbum e fazer trocas com os usuarios.

    Exemplos
    >>> c = Colecao(100)
    >>> c.insere(78)
    >>> c.insere(80)          
    >>> c.insere(3)         
    >>> c.insere(3)
    >>> c.insere(4)
    >>> c.insere(3)
    >>> c.insere(78)
    >>> c.insere(80)
    >>> c.exibir_repetidas()
    '[3 (2), 78 (1), 80 (1)]'
    >>> c1 = Colecao(100)
    >>> c1.insere(29)
    >>> c1.insere(4)
    >>> c1.insere(29)          
    >>> c1.insere(33)       
    >>> c1.insere(33)
    >>> c1.insere(29)
    >>> c1.insere(80)
    >>> c1.insere(80)
    >>> c1.insere(99)
    >>> c1.exibir_repetidas()
    '[29 (2), 33 (1), 80 (1)]'
    >>> c1.troca(c)
    >>> c.exibir_figuras()
    '[3, 4, 29, 33, 78, 80]'
    >>> c1.exibir_figuras()
    '[3, 4, 29, 33, 78, 80, 99]'
    '''

    def __init__(self, capacidade:int) :
        '''
        Cria um album.
        '''

        return NotImplemented


    def insere(self, figurinha:int):
        '''
        Insere uma figurinha especifica e ordena o album do usuario

        Requer que 0 < numerações das figurinhas < *capacidade_album*

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(58)
        >>> c.insere(12)
        >>> c.insere(75)
        >>> c.insere(2)
        >>> c.insere(33)
        >>> c.exibir_figuras()
        "[2, 12, 33, 58, 75]"
        '''

        return NotImplemented


    def remove(self,figurinha:int) -> int:
        '''
        Remove uma figurinha especifica no album do usuario.

        Requer que a figurinha esteja no album.
        Requer que o albúm não esteja vazio.

        Exemplos
        >>> c = Colecao(100)
        >>> c.remove(34)
        Traceback (most recent call last):
        ...
        ValueError: O album está vazio!
        >>> c.insere(34)
        >>> c.insere(28)
        >>> c.insere(28)
        >>> c.remove(28)
        28
        >>> c.remove(34)
        Traceback (most recent call last):
        ...
        ValueError: Não há figurinhas repetidas no album!
        >>> c.remove(14)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha não está no albúm!
        '''

        return NotImplemented


    def exibir_figuras(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes em um álbum, 
        sem considerar as repetidas de cada figurinha.

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(32)
        >>> c.insere(58)
        >>> c.insere(9)
        >>> c.insere(32)
        >>> c.exibir_figuras()
        '[9, 32, 58]'
        >>> c.remove(32)
        32
        '''

        return NotImplemented


    def exibir_repetidas(self) -> str:
        '''
        Gerar uma representação em string das figurinhas presentes em um álbum, 
        indicando a quantidade somente das figurinhas repetidas > 1.

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(58)
        >>> c.insere(58)
        >>> c.insere(58)
        >>> c.insere(9)
        >>> c.insere(32)
        >>> c.insere(32)
        >>> c.exibir_repetidas()
        '[32 (1), 58 (2)]'
        >>> c.remove(32)
        32
        >>> c.exibir_repetidas()
        '[58 (2)]'
        '''

        return NotImplemented


    def troca(self, album1:Colecao, album2:Colecao):
        '''
        Realizar a troca máxima de figurinhas entre duas coleções, garantindo que cada
        coleção obtenha as figurinhas que não possui.
        
        Exemplos
        >>> c1 = Colecao(100)
        >>> c1.insere(58)
        >>> c1.insere(58)
        >>> c1.insere(58)
        >>> c1.insere(9)
        >>> c1.insere(32)
        >>> c1.insere(32)
        >>> c1.exibir_repetidas()
        '[32 (1), 58 (2)]'
        >>> c2 = Colecao(100)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(4)
        >>> c2.insere(4)
        >>> c2.exibir_repetidas()
        '[4 (1), 60 (3)]'
        >>> c1.troca(c2)
        >>> c1.exibir_figuras()
        '[4, 9, 32, 58, 60]'
        >>> c2.exibir_figuras()
        '[4, 32, 58, 60]'
        '''

        return NotImplemented