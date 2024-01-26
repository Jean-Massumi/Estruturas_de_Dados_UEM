from __future__ import annotations
from ed import array

class Colecoes:
    '''
    Uma Coleção de figurinhas que permite gerenciar os álbuns e fazer trocas com os 
    usuarios.
    '''

    # A *capacidade_album* é uma limitacao que um album pode suportar
    # uma certa quantidade x de figurinhas sem ser repetidas nela.


    def __init__(self) :
        '''
        Criação de uma coleção com a quantidade de figurinhas(número de figurinhas total do albúm)
        '''


    def insercao(self, figurinha:int):
        '''
        Insere uma figurinha especifica no album do usuario

        Requer que 0 < numerações das figurinhas < *capacidade_album*

        Exemplos
        >>> c = Colecao()
        >>> c.insercao(58)
        >>> c.gerar_str_figuras()
        "[58]"
        >>> c.insercao(12)
        >>> c.gerar_str_figuras()
        "[12, 58]"
        >>> c.insercao(75)
        >>> c.insercao(2)
        >>> c.insercao(33)
        >>> c.gerar_str_figuras()
        "[2, 12, 33, 58, 75]"
        '''


    def remocao(self,figurinha:int) -> int:
        '''
        Remove uma figurinha especifica no album do usuario.

        Requer que a figurinha esteja no album.
        Requer que o albúm não esteja vazio.

        Exemplos
        >>> c = Colecao()
        >>> c.remocao(34)
        Traceback (most recent call last):
        ...
        ValueError: Figurinha indiponivel
        >>> c.insercao(28)
        >>> c.remocao(28)
        28
        '''


    def gerar_str_figuras(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes em um álbum, 
        sem considerar repetições.

        Exemplos
        >>> c = Colecao()
        >>> c.insercao(58)
        >>> c.insercao(9)
        >>> c.insercao(32)
        >>> c.gerar_str_figuras()
        "[9, 32, 58]"
        >>> c.remocao(32)
        32
        >>> c.gerar_str_figuras()
        "[9, 58]"
        '''


    def gerar_str_figuras_repetidas(self) -> str:
        '''
        Gerar uma representação em string das figurinhas presentes em um álbum, 
        indicando a quantidade de repetições.

        Exemplos
        >>> c = Colecao()
        >>> c.insercao(58)
        >>> c.insercao(58)
        >>> c.insercao(58)
        >>> c.insercao(9)
        >>> c.insercao(32)
        >>> c.insercao(32)
        >>> c.gerar_str_figuras_repetidas()
        "[9 (1), 32 (2), 58 (3)]"
        >>> c.remocao(32)
        32
        >>> c.gerar_str_figuras_repetidas()
        "[9 (1), 32 (1), 58 (3)]"
        '''


    def troca(self, p1:int, p2:int):
        '''
        Realizar a troca máxima de figurinhas entre duas coleções, garantindo que cada
        coleção obtenha as figurinhas que não possui.
        
        Exemplos
        # Usuario 1
        >>> c1 = Colecao()
        >>> c1.insercao(58)
        >>> c1.insercao(58)
        >>> c1.insercao(58)
        >>> c1.insercao(9)
        >>> c1.insercao(32)
        >>> c1.insercao(32)
        >>> c1.gerar_str_figuras_repetidas()
        "[9 (1), 32 (2), 58 (3)]"
        # Usuario 2
        >>> c2 = Colecao()
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(4)
        >>> c2.insercao(4)
        >>> c2.gerar_str_figuras_repetidas()
        "[4 (2), 60 (4)]"
        # Realização da Troca
        >>> c1.troca(58, 60)
        >>> c1.gerar_str_figuras_repetidas()
        "[9 (1), 32 (2), 60 (3)]"
        >>> c2.gerar_str_figuras_repetidas()
        "[4 (2), 58 (3), 60 (1)]"
        '''



