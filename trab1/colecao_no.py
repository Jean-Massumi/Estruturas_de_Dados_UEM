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
        Cria um albúm que pode suportar até certa *capacidade*.
        Cria uma *quantidade*, para gerenciar quantas figurinhas 
        sem contar as repetidas há no albúm.
        '''
        self.album = None
        self.quantidade = 0
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
        '[2, 12, 33, 58, 75]'
        '''

        if 0 > figurinha > self.capacidade:
            raise ValueError('A figurinha não está no albúm')
        
        if self.album is None:
            self.album = No(None, figurinha, +1, None)      # type: ignore
            self.quantidade += 1

        else:
            referencia = self.album
            inserido = True

            while inserido:  
                if figurinha == referencia.figurinha:
                    referencia.repetidas += 1
                    inserido = False

                elif figurinha < referencia.figurinha and referencia.antes is None:       
                    referencia.antes = No(None, figurinha, +1, referencia)
                    self.album = referencia.antes
                    self.quantidade += 1
                    inserido = False

                elif figurinha < referencia.figurinha and referencia.antes is not None:
                    referencia.antes.prox = No(referencia.antes, figurinha, +1, referencia)
                    referencia.antes = referencia.antes.prox
                    self.quantidade += 1
                    inserido = False
                            
                elif referencia.prox is None and referencia.figurinha < figurinha:
                    referencia.prox = No(referencia, figurinha, +1, None)
                    self.quantidade += 1
                    inserido = False

                referencia = referencia.prox
            

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
        ValueError: Figurinha inesistente!
        '''

        if self.album is None:
            raise ValueError('O albúm está vazio')
        
        removido = True
        referencia = self.album
        while removido: 
            if figurinha == referencia.figurinha:
                referencia.repetidas -= 1
                if referencia.repetidas == 0 and referencia.antes is None:
                    referencia.prox.antes = None
                    self.album = referencia.prox
                    self.quantidade -= 1

                elif referencia.repetidas == 0 and referencia.prox is None:
                    referencia.antes.prox = None
                    self.quantidade -= 1
                    
                elif referencia.repetidas == 0 and referencia.antes is not None:
                    referencia.antes.prox = referencia.prox
                    referencia.prox.antes = referencia.antes.prox
                    self.quantidade -= 1

                if self.quantidade == 0:
                    self.album = None

                removido = False
            else:   
                if referencia.prox is None:
                    raise ValueError('Figurinha inesistente!')

            referencia = referencia.prox

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

        referencia = self.album
        represetacao_str = '['
        if self.quantidade != 0:
            represetacao_str += str(referencia.figurinha) + f' ({referencia.repetidas})'    # type: ignore
            while referencia.prox is not None:                                              # type: ignore
                referencia = referencia.prox                                                # type: ignore
                represetacao_str += ', ' + str(referencia.figurinha) + f' ({referencia.repetidas})'     
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

        qtd_figurinhas1 = album1.quantidade
        qtd_figurinhas2 = album2.quantidade

        ref1 = album1.album
        ref2 = album2.album
    
        while ref1 is not None:
            inserido = False
            ref2 = album2.album
            while not inserido:
                if ref2 is None:
                    break
                elif ref1.figurinha == ref2.figurinha:  
                    qtd_figurinhas1 -= 1
                    qtd_figurinhas2 -= 1
                    
                    inserido = True
                ref2 = ref2.prox
            ref1 = ref1.prox

        copia_album1 = self.copia(album1.album)
        copia_album2 = self.copia(album2.album)


        if qtd_figurinhas1 < qtd_figurinhas2:
            meta = 0
            no_atual = copia_album2
            while no_atual is not None and meta != qtd_figurinhas1:
                # Verifica se o valor já está na lista de destino
                if not self.valor_existe_no(copia_album1, no_atual.figurinha):
                    album1.insere(no_atual.figurinha)
                    album2.remove(no_atual.figurinha)
                    meta += 1
                no_atual = no_atual.prox

            # meta = 0
            no_atual = copia_album1
            while no_atual is not None and meta != qtd_figurinhas1:
                # Verifica se o valor já está na lista de destino
                if not self.valor_existe_no(copia_album2, no_atual.figurinha):
                    album2.insere(no_atual.figurinha)
                    album1.remove(no_atual.figurinha)
                    meta += 1
                no_atual = no_atual.prox

        else:
            meta = 0
            no_atual = copia_album2
            while no_atual is not None and meta != qtd_figurinhas2:
                # Verifica se o valor já está na lista de destino
                if not self.valor_existe_no(copia_album1, no_atual.figurinha):
                    album1.insere(no_atual.figurinha)
                    album2.remove(no_atual.figurinha)
                    meta += 1
                no_atual = no_atual.prox

            meta = 0
            no_atual = copia_album1
            while no_atual is not None and meta != qtd_figurinhas2:
                # Verifica se o valor já está na lista de destino
                if not self.valor_existe_no(copia_album2, no_atual.figurinha):
                    album2.insere(no_atual.figurinha)
                    album1.remove(no_atual.figurinha)
                    meta += 1
                no_atual = no_atual.prox

    

    def valor_existe_no(self, no: No, item):
        '''
            Verifica se um valor de uma lista encadeada existe em uma outra lista encadeada. 
        '''

        no_atual = no
        while no_atual is not None:
            if no_atual.figurinha == item:
                return True
            no_atual = no_atual.prox
        return False


    def copia(self, no: No) -> No:
        '''
        Cria uma copia do encadeamento de entrada.
        '''

        copia3 = None

        while no is not None:
            if not self.valor_existe_no(copia3, no.figurinha):
                if copia3 is None:
                    copia3 = No(None, no.figurinha, 1, None)
                else:
                    referencia = copia3

                    while referencia.prox is not None:
                        referencia = referencia.prox

                    referencia.prox = No(referencia, no.figurinha, 1, None)

            no = no.prox
        return copia3

c = Colecao(100)
c.insere(78)
c.insere(13)
c.insere(58)
c.insere(80)          
c.insere(81)         
c.insere(3)
c.insere(4)
c.insere(3)
c.insere(78)
c.insere(80)
c1 = Colecao(100)
c1.insere(4)
c1.insere(78)
c1.insere(58)
c1.insere(81)          
c1.insere(33)       
c1.insere(33)
c1.insere(29)
c1.insere(76)
c1.insere(76)
c1.insere(99)
c1.troca(c, c1)
c.exibir_repetidas()
'[3 (1), 4 (1), 29 (1), 33 (1), 58 (1), 76 (1), 78 (2), 80 (1), 81 (1)]'
c1.exibir_repetidas()
'[3 (1), 4 (1), 13 (1), 33 (1), 58 (1), 76 (1), 78 (1), 80 (1), 81 (1), 99 (1)]'
