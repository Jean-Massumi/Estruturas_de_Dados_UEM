from __future__ import annotations
from ed import array

class Colecao:
    '''
    Uma Coleção de figurinhas que permite gerenciar
    o álbum e fazer trocas com os usuarios.

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
        Cria um album com *capacidade* e outro para armazenar  
        a quantidade de repetidas contidas no primeiro albúm.

        Os albúns devem ter uma contagem de indice para saber quantas 
        novas figuras foram adicionada no array.
        '''

        self.capacidade = capacidade
        self.album = array(self.capacidade + 1, 0)
        self.indice = 0
        self.repetidas = array(self.capacidade + 1, 0)
        self.indice_repetidas = 0


    def insere(self, figurinha:int):
        '''
        Insere e ordena uma figurinha especifica no album do usuario.

        Requer que 0 < numerações das figurinhas < *capacidade_album*
        
        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(58)
        >>> c.insere(12)
        >>> c.insere(75)
        >>> c.insere(2)
        >>> c.insere(33)
        >>> c.exibir_figuras()
        '[2, 12, 33, 58, 75]'
        '''
        
        if figurinha > self.capacidade or figurinha < 0:
            raise ValueError('Figurinha com enumeração inexistente!')
        
        for i in range(self.indice, -1, -1):
            if figurinha not in self.album:
                if figurinha < self.album[i - 1]:
                    # Se a figurinha for < que a figurinha referente ao
                    # indice do *album*. A figurinha do *album* 
                    # é movido pro proximo indice. 
                    self.album[i] = self.album[i - 1]
                    self.repetidas[i] = self.repetidas[i - 1]
                elif figurinha > self.album[i - 1]:
                    # Se a figurinha > que figurinha referente ao indice do *album*.
                    self.album[i] = figurinha
                    self.indice += 1
                    self.repetidas[i] = 0
                    self.repetidas[i] += 1
                    self.indice_repetidas += 1
            else:
                # Se a figurinha estiver no album, essa condição acontece.
                if figurinha == self.album[i]:
                    # A figurinha percorre pelo *album* principal até
                    # achar a figurinha igual a ela.
                    # Encontrado a figurinha igual a ela, soma mais 1
                    # no *album_repetidas* referente ao indice
                    # do *album* principal.
                    self.repetidas[i] += 1



    def remove(self, figurinha:int) -> int:
        '''
        Remove uma figurinha especifica no album do 
        usuario e devolve a figurinha removida.

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

        if self.indice == 0:
            raise ValueError('O albúm está vazio')

        if figurinha not in self.album:
            raise ValueError('A figurinha não está no albúm')
        else:
            for i in range(self.indice):
                if figurinha == self.album[i]:
                    # Remove -1 figurinha no *album_repetidas* se 
                    # a figurinha for igual a figurinha que
                    # está no *album* principal.
                    self.repetidas[i] -= 1
                    if self.repetidas[i] == 0:
                        # Caso o *album_repetidas* no indice referido 
                        # for igual a 0. O valor do indice *album* 
                        # principal e o *album_repetidas* é movido para 
                        # o lugar da figurinha que ficou igual a 0.
                        self.album[i] = self.album[i + 1]
                        self.repetidas[i] = self.repetidas[i + 1]
                        self.indice -= 1
                        self.indice_repetidas -= 1

                elif figurinha not in self.album:
                    # Como a condição acima executa somente uma vez,
                    # essa condicao irá fazer o restante da ordenação.
                    self.album[i] = self.album[i + 1]
                    self.repetidas[i] = self.repetidas[i + 1]
        
        return figurinha


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
        '[9, 32, 58]'
        >>> c.remove(32)
        32
        >>> c.exibir_figuras()
        '[9, 58]'
        '''

        represetacao_str = '['
        if self.indice != 0:
            represetacao_str += str(self.album[0])
            for i in range(1, self.indice):
                represetacao_str += ', ' + str(self.album[i])
        return represetacao_str + ']'


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
        '[9 (1), 32 (2), 58 (3)]'
        >>> c.remove(32)
        32
        >>> c.exibir_repetidas()
        '[9 (1), 32 (1), 58 (3)]'
        '''

        represetacao_str = '['
        if self.indice != 0:
            represetacao_str += str(self.album[0]) + f' ({self.repetidas[0]})'
            for i in range(1, self.indice):
                represetacao_str += ', ' + str(self.album[i]) + f' ({self.repetidas[i]})'
        return represetacao_str + ']'



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

        # As *trocas_possiveis* será usado para armazenar as 
        # figurinhas que nao estao em um album1 no album2 e vice-versa.
        trocas_possiveis1 = array(self.capacidade, 0)
        indice1 = 0
        trocas_possiveis2 = array(self.capacidade, 0)
        indice2 = 0

        for num in album1.album:
            if num == 0:
                break
            elif num not in album2.album:
                # Insere *num* na *trocas_possiveis1* se o *num* nao estiver no *album2*
                trocas_possiveis1[indice1] = num
                indice1 += 1

        for num in album2.album:
            if num == 0:
                break
            elif num not in album1.album:
                # Insere *num* na *trocas_possiveis2* se o *num* nao estiver no *album1*
                trocas_possiveis2[indice2] = num
                indice2 += 1

        # Pega a menor troca possivel entre duas coleções.
        if indice1 <= indice2:
            for i in range(indice1):
                album1.insere(trocas_possiveis2[i])
                # Faz a insercao da figurinha do *album2* no *album1*
                album2.insere(trocas_possiveis1[i])
                # Faz a remocao da figurinha(figurinha que foi inserido no album1) no *album2* .
                album1.remove(trocas_possiveis1[i])
                album2.remove(trocas_possiveis2[i])
        elif indice2 < indice1:
            for i in range(indice2):
                album1.insere(trocas_possiveis2[i])
                album2.insere(trocas_possiveis1[i])
                album1.remove(trocas_possiveis1[i])
                album2.remove(trocas_possiveis2[i])