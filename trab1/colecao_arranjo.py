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
        Cria um album com *capacidade* e outro para armazenar  
        a quantidade de repetidas contidas no primeiro albúm.

        Os albúns devem ter uma contagem de indice para saber quantas 
        novas figuras foram adicionada no array.
        '''

        self.capacidade = capacidade
        self.album = array(self.capacidade + 1, 0)
        self.indice = 0
        self.repetidas = array(self.capacidade + 1, -1)
        self.indice_repetidas = 0


    def insere(self, figurinha:int):
        '''
        Insere uma figurinha especifica e ordena o album do usuario.

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
                    self.repetidas[i - 1] = -1
                    self.repetidas[i - 1] += 1
                elif figurinha > self.album[i - 1]:
                    # Se a figurinha > que figurinha referente ao indice do *album*.
                    self.album[i] = figurinha
                    self.indice += 1
                    self.repetidas[i] = -1
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

        if self.indice == 0:
            raise ValueError('O album está vazio!')

        if figurinha not in self.album:
            raise ValueError('A figurinha não está no albúm!')
        
        else:
            for i in range(self.indice):
                if figurinha == self.album[i] and self.repetidas[i] > 0:
                    self.repetidas[i] -= 1
                
                elif figurinha == self.album[i] and self.repetidas[i] == 0:
                    raise ValueError('Não há figurinhas repetidas no album!')
                
        return figurinha  


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

        represetacao_str = '['
        if self.indice != 0:
            represetacao_str += str(self.album[0])
            for i in range(1, self.indice):
                represetacao_str += ', ' + str(self.album[i])
        return represetacao_str + ']'


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

        adicionado = 1
        represetacao_str = '['
        if self.indice != 0:
            for i in range(0, self.indice):
                if self.repetidas[i] > 0 and adicionado == 1:
                    represetacao_str += str(self.album[i]) + f' ({self.repetidas[i]})'
                    adicionado -= 1

                elif self.repetidas[i] > 0:
                    represetacao_str += ', ' + str(self.album[i]) + f' ({self.repetidas[i]})'

        return represetacao_str + ']'


    def troca(self, album1:Colecao):
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

        # As *trocas_possiveis* será usado para armazenar as 
        # figurinhas que nao estao em um album1 no album2 e vice-versa.
        trocas_possiveis1 = array(self.capacidade, 0)
        indice1 = 0
        trocas_possiveis2 = array(self.capacidade, 0)
        indice2 = 0

        for i in range(album1.indice):
            if album1.album[i] not in self.album and album1.repetidas[i] > 0:
                # Insere *num* na *trocas_possiveis1* se o *num* nao estiver no *album2*
                trocas_possiveis1[indice1] = album1.album[i]
                indice1 += 1

        for j in range(self.indice):
            if self.album[j] not in album1.album and self.repetidas[j] > 0:
                # Insere *num* na *trocas_possiveis2* se o *num* nao estiver no *album1*
                trocas_possiveis2[indice2] = self.album[j]
                indice2 += 1

        # Pega a menor troca possivel entre duas coleções.
        if indice1 <= indice2:
            for i in range(indice1):
                album1.insere(trocas_possiveis2[i])
                # Faz a insercao da figurinha do *album2* no *album1*
                self.insere(trocas_possiveis1[i])
                # Faz a remocao da figurinha(figurinha que foi inserido no album1) no *album2* .
                album1.remove(trocas_possiveis1[i])
                self.remove(trocas_possiveis2[i])
        elif indice2 < indice1:
            for i in range(indice2):
                album1.insere(trocas_possiveis2[i])
                self.insere(trocas_possiveis1[i])
                album1.remove(trocas_possiveis1[i])
                self.remove(trocas_possiveis2[i])