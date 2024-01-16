from enum import Enum

class Dia(Enum):
    '''
    Um dia da semana.
    '''
    DOM = 0
    SEG = 1
    TER = 2
    QUA = 3
    QUI = 4
    SEX = 5
    SAB = 6


class Dias:
    '''
    Um conjunto de dias da semana que um evento deve se repetir.
    '''
    lista_dias = []

    def __init__(self):
        '''
        Cria um novo conjunto vazio de dias.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        '''

        self.lista_dias = list()

        return

    def alterna(self, d: Dia):
        '''
        Alterna a pertinencia do dia *d* em *self*, isto é, se *d* está em
        *self*, *d* é removido. Se *d* não está em *self*, *d* é adicionado.

        Exemplos
        >>> c = Dias()
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['sex']
        >>> c.alterna(Dia.SEG)
        >>> c.lista()
        ['seg', 'sex']
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['seg']
        '''

        if d.value not in self.lista_dias:
            self.lista_dias.append(d.value)
        else:
            self.lista_dias.remove(d.value)



    def lista(self) -> list[str]:
        '''
        Devolve uma lista com os dias (abreviações) em ordem da semana que
        estão em *self*.

        Exemplos
        >>> c = Dias()
        >>> c.lista()
        []
        >>> c.alterna(Dia.TER)
        >>> c.lista()
        ['ter']
        >>> c.alterna(Dia.DOM)
        >>> c.lista()
        ['dom', 'ter']
        >>> c.alterna(Dia.QUI)
        >>> c.alterna(Dia.SEG)
        >>> c.alterna(Dia.SAB)
        >>> c.alterna(Dia.QUA)
        >>> c.alterna(Dia.SEX)
        >>> c.lista()
        ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        '''
        
        self.lista_dias.sort()
        dias_ativos = []
        dia_semana = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

        for i in self.lista_dias:
            for j in range(7):
                if i == j:
                    dias_ativos.append(dia_semana[i])


        return dias_ativos
