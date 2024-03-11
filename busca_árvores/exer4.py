from dataclasses import dataclass

@dataclass
class Item:
    chave: str
    valor: int


class Dicionario:
    '''
    Uma coleção de associações chave-valor, onde
    cada chave é única
    
    Exemplos:
    >>> d = Dicionario()
    >>> d.num_itens()
    0
    >>> d.associa('Jorge', 25)
    >>> d.associa('Bia', 40)
    >>> d.num_itens()
    2
    >>> d.get('Jorge')
    25
    >>> d.get('Bia')
    40
    >>> d.get('Andre') is None
    True
    >>> d.associa('Bia', 50)
    >>> d.get('Bia')
    50
    >>> d.remove('Jorge')
    >>> d.get('Jorge') is None
    True
    >>> d.remove('Ana')
    '''

    itens= list[Item]

    def __init__(self):
        self.itens = []


    def num_itens(self) -> int:
        '''
        Devolve a quantidade de chaves no dicionário.
        '''

        return len(self.itens)
    

    def busca(self, chave: str, inicio: int, fim:int) -> int | None:
        '''
        Devolve True se *n* está na lista, False caso contrario.

        A lista deve está ordenada para usar a busca binaria.

        '''
  
        if inicio > fim:
            return None
        else:
            m = (inicio + fim)//2
            if chave == self.itens[m].chave :
                return m
            elif chave < self.itens[m].chave:
                return self.busca(chave, inicio, m - 1)
            elif chave > self.itens[m].chave:
                return self.busca(chave, m + 1, fim)
    
    

    def associa(self, chave: str, valor: int):
        '''
        Associa a *chave* com o *valor* no dicionário.
        Se *chave* já está associada com um valor, ele
        é sustituído por *valor*.
        '''

        i = self.busca(chave, 0, len(self.itens) - 1)
        if i is not None:
            self.itens[i].valor = valor
        else:
            self.itens.append(Item(chave, valor))


    def get(self, chave: str) -> int | None:
        ''' 
        Devolve o valor associado com *chave* no dicionário ou None se a chave não está no dicionário.
        '''

        i = self.busca(chave, 0, len(self.itens) - 1)
        if i is not None:
            return self.itens[i].valor
        else:
            return None

    def remove(self, chave: str):
        ''' 
        Remove a *chave* e o valor associado com ela do
        dicionário. Não faz nada se a *chave* não está no
        dicionário.
        '''















