from __future__ import annotations
from ed import array

class Colecao:
    '''
    Uma Coleção de figurinhas que permite gerenciar os álbuns e fazer trocas com os 
    usuarios.

    Exemplos
    >>> c = Colecao()
    >>> c.insercao(78)
    >>> c.insercao(13)
    >>> c.insercao(58)
    >>> c.insercao(80)          
    >>> c.insercao(81)         
    >>> c.insercao(3)
    >>> c.insercao(4)
    >>> c.insercao(3)
    >>> c.insercao(78)
    >>> c.insercao(80)
    >>> c.gerar_str_figuras_repetidas()
    '[3 (2), 4 (1), 13 (1), 58 (1), 78 (2), 80 (2), 81 (1)]'
    >>> c1 = Colecao()
    >>> c1.insercao(4)
    >>> c1.insercao(78)
    >>> c1.insercao(58)
    >>> c1.insercao(81)          
    >>> c1.insercao(33)       
    >>> c1.insercao(33)
    >>> c1.insercao(29)
    >>> c1.insercao(76)
    >>> c1.insercao(76)
    >>> c1.insercao(99)
    >>> c1.gerar_str_figuras_repetidas()
    '[4 (1), 29 (1), 33 (2), 58 (1), 76 (2), 78 (1), 81 (1), 99 (1)]'
    >>> c1.troca(c, c1)
    >>> c.gerar_str_figuras_repetidas()
    '[3 (1), 4 (1), 29 (1), 33 (1), 58 (1), 76 (1), 78 (2), 80 (1), 81 (1)]'
    >>> c1.gerar_str_figuras_repetidas()
    '[3 (1), 4 (1), 13 (1), 33 (1), 58 (1), 76 (1), 78 (1), 80 (1), 81 (1), 99 (1)]'
    >>> c.remocao(4)
    4
    >>> c.remocao(58)
    58
    >>> c.remocao(76)
    76
    >>> c.remocao(78)
    78
    >>> c.gerar_str_figuras_repetidas()
    '[3 (1), 29 (1), 33 (1), 78 (1), 80 (1), 81 (1)]'
    >>> c.gerar_str_figuras()
    '[3, 29, 33, 78, 80, 81]'
    '''

    capacidade_album = 100
    # A *capacidade_album* é uma limitacao que um album pode suportar
    # uma certa quantidade de figurinhas enumeradas(1,2,3,4...) nela.


    def __init__(self) :
        '''
        Cria um album com *capacidade_album* e outro para armazenar a quantidade de repetidas contidas no   
        primeiro albúm.

        Os albúns devem ter uma contagem de indice para saber quantas novas figuras foram adicionada no array.
        '''

        self.album = array(self.capacidade_album + 1, 0)
        self.indice_album = 0
        self.album_repetidas = array(self.capacidade_album + 1, 0)
        self.indice_album_repetidas = 0


    def insercao(self, figurinha:int):
        '''
        Insere e ordena uma figurinha especifica no album do usuario.

        Requer que 0 < numerações das figurinhas < *capacidade_album*
        
        Exemplos
        >>> c = Colecao()
        >>> c.insercao(58)
        >>> c.insercao(12)
        >>> c.insercao(75)
        >>> c.insercao(2)
        >>> c.insercao(33)
        >>> c.gerar_str_figuras()
        '[2, 12, 33, 58, 75]'
        '''
        
        if figurinha > self.capacidade_album or figurinha < 0:
            raise ValueError('Figurinha com enumeração inexistente!')
        
        for i in range(self.indice_album, -1, -1):
            if figurinha not in self.album:
                if figurinha < self.album[i - 1]:
                    self.album[i] = self.album[i - 1]
                    self.album_repetidas[i] = self.album_repetidas[i - 1]
                elif figurinha > self.album[i - 1]:
                    self.album[i] = figurinha
                    self.indice_album += 1
                    self.album_repetidas[i] = 0
                    self.album_repetidas[i] += 1
                    self.indice_album_repetidas += 1
            else: 
                if figurinha == self.album[i]:
                    self.album_repetidas[i] += 1



    def remocao(self, figurinha:int) -> int:
        '''
        Remove uma figurinha especifica no album do usuario e devolve a figurinha removida.

        Requer que a figurinha esteja no album.
        Requer que o albúm não esteja vazio.

        Exemplos
        >>> c = Colecao()
        >>> c.remocao(34)
        Traceback (most recent call last):
        ...
        ValueError: O albúm está vazio
        >>> c.insercao(28)
        >>> c.insercao(11)
        >>> c.remocao(28)
        28
        >>> c.remocao(33)
        Traceback (most recent call last):
        ...
        ValueError: A figurinha não está no albúm
        '''

        if self.indice_album == 0:
            raise ValueError('O albúm está vazio')

        if figurinha not in self.album:
            raise ValueError('A figurinha não está no albúm')
        else:
            for i in range(self.indice_album):
                if figurinha == self.album[i]:
                    self.album_repetidas[i] -= 1
                    if self.album_repetidas[i] == 0:
                        self.album[i] = self.album[i + 1]
                        self.album_repetidas[i] = self.album_repetidas[i + 1]
                        self.indice_album -= 1
                        self.indice_album_repetidas -= 1

                elif figurinha not in self.album:
                    self.album[i] = self.album[i + 1]
                    self.album_repetidas[i] = self.album_repetidas[i + 1]
        
        return figurinha


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
        '[9, 32, 58]'
        >>> c.remocao(32)
        32
        >>> c.gerar_str_figuras()
        '[9, 58]'
        '''

        represetacao_str = '['
        if self.indice_album != 0:
            represetacao_str += str(self.album[0])
            for i in range(1, self.indice_album):
                represetacao_str += ', ' + str(self.album[i])
        return represetacao_str + ']'


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
        '[9 (1), 32 (2), 58 (3)]'
        >>> c.remocao(32)
        32
        >>> c.gerar_str_figuras_repetidas()
        '[9 (1), 32 (1), 58 (3)]'
        '''

        represetacao_str = '['
        if self.indice_album != 0:
            represetacao_str += str(self.album[0]) + f' ({self.album_repetidas[0]})'
            for i in range(1, self.indice_album):
                represetacao_str += ', ' + str(self.album[i]) + f' ({self.album_repetidas[i]})'
        return represetacao_str + ']'



    def troca(self, album1:Colecao, album2:Colecao):
        '''
        Realizar a troca máxima de figurinhas entre duas coleções, garantindo que cada
        coleção obtenha as figurinhas que não possui.
        
        Exemplos
        >>> c1 = Colecao()
        >>> c1.insercao(58)
        >>> c1.insercao(58)
        >>> c1.insercao(58)
        >>> c1.insercao(9)
        >>> c1.insercao(32)
        >>> c1.insercao(32)
        >>> c1.gerar_str_figuras_repetidas()
        '[9 (1), 32 (2), 58 (3)]'
        >>> c2 = Colecao()
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(60)
        >>> c2.insercao(4)
        >>> c2.insercao(4)
        >>> c2.gerar_str_figuras_repetidas()
        '[4 (2), 60 (4)]'
        >>> c1.troca(c1, c2)
        >>> c1.gerar_str_figuras_repetidas()
        '[4 (1), 32 (1), 58 (3), 60 (1)]'
        >>> c2.gerar_str_figuras_repetidas()
        '[4 (1), 9 (1), 32 (1), 60 (3)]'
        '''

        trocas_possiveis1 = array(self.capacidade_album, 0)
        indice1 = 0
        trocas_possiveis2 = array(self.capacidade_album, 0)
        indice2 = 0

        for num in album1.album:
            if num == 0:
                break
            elif num not in album2.album:
                trocas_possiveis1[indice1] = num
                indice1 += 1

        for num in album2.album:
            if num == 0:
                break
            elif num not in album1.album:
                trocas_possiveis2[indice2] = num
                indice2 += 1

        if indice1 <= indice2:
            for i in range(indice1):
                album1.insercao(trocas_possiveis2[i])
                album2.insercao(trocas_possiveis1[i])
                album1.remocao(trocas_possiveis1[i])
                album2.remocao(trocas_possiveis2[i])
        elif indice2 < indice1:
            for i in range(indice2):
                album1.insercao(trocas_possiveis2[i])
                album2.insercao(trocas_possiveis1[i])
                album1.remocao(trocas_possiveis1[i])
                album2.remocao(trocas_possiveis2[i])