from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    figurinha: int
    prox: No | None


class Colecoes:
    '''
    Uma Coleção de figurinhas que permite gerenciar os álbuns e fazer trocas com os 
    usuarios.

    Exemplos
    >>> c = Colecao(100)
    >>> c.insere(78)
    >>> c.insere(13)
    >>> c.insere(58)
    >>> c.insere(80)          
    >>> c.insere(81)         
    >>> c.insere(3)
    >>> c.insere(4)
    >>> c.insere(3)
    >>> c.insere(78)
    >>> c.insere(80)
    >>> c.exibir_repetidas()
    '[3 (2), 4 (1), 13 (1), 58 (1), 78 (2), 80 (2), 81 (1)]'
    >>> c1 = Colecao(100)
    >>> c1.insere(4)
    >>> c1.insere(78)
    >>> c1.insere(58)
    >>> c1.insere(81)          
    >>> c1.insere(33)       
    >>> c1.insere(33)
    >>> c1.insere(29)
    >>> c1.insere(76)
    >>> c1.insere(76)
    >>> c1.insere(99)
    >>> c1.exibir_repetidas()
    '[4 (1), 29 (1), 33 (2), 58 (1), 76 (2), 78 (1), 81 (1), 99 (1)]'
    >>> c1.troca(c, c1)
    >>> c.exibir_repetidas()
    '[3 (1), 4 (1), 29 (1), 33 (1), 58 (1), 76 (1), 78 (2), 80 (1), 81 (1)]'
    >>> c1.exibir_repetidas()
    '[3 (1), 4 (1), 13 (1), 33 (1), 58 (1), 76 (1), 78 (1), 80 (1), 81 (1), 99 (1)]'
    >>> c.remove(4)
    4
    >>> c.remove(58)
    58
    >>> c.remove(76)
    76
    >>> c.remove(78)
    78
    >>> c.exibir_repetidas()
    '[3 (1), 29 (1), 33 (1), 78 (1), 80 (1), 81 (1)]'
    >>> c.exibir_figuras()
    '[3, 29, 33, 78, 80, 81]'
    '''

    def __init__(self, capacidade:int) :
        '''
        Cria um albúm fazio.
        '''

        self.album = None
        self.prox = No
        self.indice = 0
        self.capacidade = capacidade

    def insere(self, figurinha:int):
        '''
        Insere uma figurinha especifica no album do usuario

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

        if 0 > figurinha > self.capacidade:
            raise ValueError('A figurinha não está no albúm')
        
        if self.indice == self.capacidade:
            raise ValueError('O albúm está cheio')
        

        self.nova_figura = No(figurinha, None)
        if self.album is None:
            self.album = self.nova_figura
        else:
            atual = self.album
            inserido = True
            while atual.prox is not None and inserido:
                atual = atual.prox
                item = atual.figurinha
                if figurinha < item:
                    atual = No(self.nova_figura, atual)
                    inserido = False
                    
            


        

                
    


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
        ValueError: O albúm está vazio
        >>> c.insere(28)
        >>> c.insere(11)
        >>> c.remove(28)
        28
        >>> c.remove(33)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha não está no albúm
        '''


    def exibir_figuras(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes em um álbum, 
        sem considerar repetições.

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(58)
        >>> c.insere(9)
        >>> c.insere(32)
        >>> c.exibir_figuras()
        "[9, 32, 58]"
        >>> c.remove(32)
        32
        >>> c.exibir_figuras()
        "[9, 58]"
        '''


    def exibir_repetidas(self) -> str:
        '''
        Gerar uma representação em string das figurinhas presentes em um álbum, 
        indicando a quantidade de repetições.

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(58)
        >>> c.insere(58)
        >>> c.insere(58)
        >>> c.insere(9)
        >>> c.insere(32)
        >>> c.insere(32)
        >>> c.exibir_repetidas()
        "[9 (1), 32 (2), 58 (3)]"
        >>> c.remove(32)
        32
        >>> c.exibir_repetidas()
        "[9 (1), 32 (1), 58 (3)]"
        '''


    def troca(self, album1:int, album2:int):
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
        '[9 (1), 32 (2), 58 (3)]'
        >>> c2 = Colecao(100)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(4)
        >>> c2.insere(4)
        >>> c2.exibir_repetidas()
        '[4 (2), 60 (4)]'
        >>> c1.troca(c1, c2)
        >>> c1.exibir_repetidas()
        '[4 (1), 32 (1), 58 (3), 60 (1)]'
        >>> c2.exibir_repetidas()
        '[4 (1), 9 (1), 32 (1), 60 (3)]'
        '''











