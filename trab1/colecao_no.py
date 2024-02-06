from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    antes: No | None            
    figurinha: int
    repetidas: int
    prox: No | None

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
    >>> c.exibir_figuras()
    '[3, 4, 78, 80]'
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
    >>> c1.exibir_figuras()
    '[4, 29, 33, 80, 99]'
    >>> c1.exibir_repetidas()
    '[29 (2), 33 (1), 80 (1)]'
    
    >>> c1.troca(c)
    >>> c.exibir_figuras()
    '[3, 4, 29, 33, 78, 80]'
    >>> c.exibir_repetidas()
    '[3 (1), 80 (1)]'
    >>> c.remove(3)
    3
    >>> c.remove(80)
    80
    >>> c.exibir_repetidas()
    '[]'

    >>> c1.exibir_figuras()
    '[3, 4, 29, 33, 78, 80, 99]'
    >>> c1.exibir_repetidas()
    '[29 (1), 80 (1)]'
    >>> c1.remove(29)
    29
    >>> c1.remove(80)
    80
    >>> c1.exibir_repetidas()
    '[]'
    '''

    album : No | None
    quantidade : int

    def __init__(self, capacidade:int) :
        '''
        Cria um albúm vazio que pode suportar até certa *capacidade*.
        '''
        self.album = None
        self.quantidade = 0
        # Cria uma *quantidade*, para gerenciar quantas figurinhas 
        # sem contar as repetidas há no albúm.
        self.capacidade = capacidade


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
        '[2, 12, 33, 58, 75]'
        '''

        if 0 > figurinha > self.capacidade:
            raise ValueError('A figurinha não está no albúm')
        
        if self.album is None:
            self.album = No(None, figurinha, +1, None)     
            self.quantidade += 1

        else:
            referencia: No | None = self.album
            inserido = False

            while not inserido and referencia is not None:  
                if figurinha == referencia.figurinha:
                    referencia.repetidas += 1
                    inserido = True

                elif figurinha < referencia.figurinha and referencia.antes is None:       
                    referencia.antes = No(None, figurinha, +1, referencia)
                    self.album = referencia.antes
                    self.quantidade += 1
                    inserido = True

                elif figurinha < referencia.figurinha and referencia.antes is not None:
                    referencia.antes.prox = No(referencia.antes, figurinha, +1, referencia)
                    referencia.antes = referencia.antes.prox
                    self.quantidade += 1
                    inserido = True
                            
                elif referencia.prox is None and referencia.figurinha < figurinha:
                    referencia.prox = No(referencia, figurinha, +1, None)
                    self.quantidade += 1
                    inserido = True

                referencia = referencia.prox
            

    def remove(self, figurinha:int):
        '''
        Remove uma figurinha especifica no album do usuario.

        Requer que a figurinha esteja no album.
        Requer que haja figurinhas repetidas para remover.
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
        ValueError: A figurinha não está no album!
        '''

        if self.album is None:
            raise ValueError('O album está vazio!')
        
        referencia : No | None = self.album
        while referencia is not None: 
            if figurinha == referencia.figurinha and referencia.repetidas > 1:
                referencia.repetidas -= 1
                return figurinha

            elif figurinha == referencia.figurinha and referencia.repetidas == 1:
                raise ValueError('Não há figurinhas repetidas no album!')
            
            elif referencia.prox is None:
                raise ValueError('A figurinha não está no album!')

            referencia = referencia.prox

        
    def exibir_figuras(self) -> str:
        '''
        Gera uma representação em string das figurinhas presentes em um álbum, 
        sem considerar repetições.

        Exemplos
        >>> c = Colecao(100)
        >>> c.insere(32)
        >>> c.insere(58)
        >>> c.insere(9)
        >>> c.insere(32)
        >>> c.exibir_figuras()
        '[9, 32, 58]'
        ''' 

        referencia = self.album
        represetacao_str = '['
        if self.quantidade != 0:
            represetacao_str += str(referencia.figurinha)           # type: ignore
            while referencia.prox is not None:                      # type: ignore
                referencia = referencia.prox                        # type: ignore
                represetacao_str += ', ' + str(referencia.figurinha)
        return represetacao_str + ']'


    def exibir_repetidas(self) -> str:
        '''
        Gerar uma representação em string das figurinhas presentes em um álbum, 
        representando as figurinhas repetidas na coleção

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

        caso1 = False
        referencia = self.album
        represetacao_str = '['
        if self.quantidade != 0:
            while referencia is not None:                                              # type: ignore
                if referencia.repetidas > 1 and not caso1:
                    # Essa condição só irá acontecer uma vez, para que haja
                    # uma organizacao na hora de exibir.
                    represetacao_str += str(referencia.figurinha) + f' ({referencia.repetidas -1})'    # type: ignore
                    caso1 = True

                elif referencia.repetidas > 1:
                    represetacao_str += ', ' + str(referencia.figurinha) + f' ({referencia.repetidas -1})'    
                referencia = referencia.prox                                                # type: ignore 
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
        >>> c1.exibir_figuras()
        '[9, 32, 58]'
        >>> c1.exibir_repetidas()
        '[32 (1), 58 (2)]'

        >>> c2 = Colecao(100)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(60)
        >>> c2.insere(4)
        >>> c2.insere(4)
        >>> c2.exibir_figuras()
        '[4, 60]'
        >>> c2.exibir_repetidas()
        '[4 (1), 60 (3)]'

        >>> c1.troca(c2)
        >>> c1.exibir_figuras()
        '[4, 9, 32, 58, 60]'
        >>> c1.exibir_repetidas()
        '[58 (1)]'

        >>> c2.exibir_figuras()
        '[4, 32, 58, 60]'
        >>> c2.exibir_repetidas()
        '[60 (2)]'
        '''

        troca_maxima1 = album1.quantidade
        troca_maxima2 = self.quantidade

        ref1 = album1.album

        while ref1 is not None:
            if self.__valor_existe_no(self.album, ref1.figurinha):
                troca_maxima1 -= 1
                troca_maxima2 -= 1
            ref1 = ref1.prox

        if troca_maxima1 <= troca_maxima2:
            self.__auxilia_trocas(album1, troca_maxima1)

        else:
            self.__auxilia_trocas(album1, troca_maxima2)
        

    def __auxilia_trocas(self, album:Colecao, maximo_troca:int):
        '''
        Devolve as trocas maximas de dois albuns.
        '''

        copia_album1 = self.__copia(album.album)
        copia_album2 = self.__copia(self.album)

        meta = 0
        no_atual: No | None = copia_album2
        while no_atual is not None and meta != maximo_troca:
            # Verifica se o valor já está na lista de destino
            if not self.__valor_existe_no(copia_album1, no_atual.figurinha) and copia_album2.repetidas > 1:    # type:ignore
                album.insere(no_atual.figurinha)
                self.remove(no_atual.figurinha)
                meta += 1
            no_atual = no_atual.prox
            copia_album2 = copia_album2.prox             # type:ignore

        meta = 0
        no_atual = copia_album1
        while no_atual is not None and meta != maximo_troca:
            # Verifica se o valor já está na lista de destino
            if not self.__valor_existe_no(copia_album2, no_atual.figurinha)  and copia_album1.repetidas > 1:   # type:ignore
                self.insere(no_atual.figurinha)
                album.remove(no_atual.figurinha)
                meta += 1
            no_atual = no_atual.prox
            copia_album1 = copia_album1.prox            # type:ignore

    
    def __valor_existe_no(self, no: No | None, item):
        '''
            Verifica se uma figurinha existe em um outro album. 
        '''

        no_atual = no
        while no_atual is not None:
            if no_atual.figurinha == item:
                return True
            no_atual = no_atual.prox
        return False


    def __copia(self, no: No | None) -> No | None:
        '''
        Cria uma copia do encadeamento de entrada.
        '''

        copia3 = None

        while no is not None:
            if not self.__valor_existe_no(copia3, no.figurinha):
                if copia3 is None:
                    if no.repetidas > 1:
                        copia3 = No(None, no.figurinha, 2, None)
                    elif no.repetidas == 1:
                        copia3 = No(None, no.figurinha, 1, None)
                else:
                    referencia = copia3

                    while referencia.prox is not None:
                        referencia = referencia.prox
                        
                    if no.repetidas > 1:
                        referencia.prox = No(referencia, no.figurinha, 2, None)
                    elif no.repetidas == 1:
                        referencia.prox = No(referencia, no.figurinha, 1, None)

            no = no.prox
        return copia3