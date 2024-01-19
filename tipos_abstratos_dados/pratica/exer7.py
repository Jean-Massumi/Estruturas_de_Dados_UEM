class BancoHoras:
    '''
        Registro/consulta de horas extras depositados em um banco de horas
    '''


    def __init__(self, minutos:int):
        '''
            Cria um armazenamento de minutos extras de um funcionario.

            Os minutos serao representados por valores inteiros positivos.         

        Exemplos:
        >>> h = BancoHoras(300)
        >>> h.consulta()
        '05:00'
        >>> h = BancoHoras(-53)
        Traceback (most recent call last):
        ...
        ValueError: Minutos em tempo negativo
    
        '''

        if minutos >= 0:
            self.minutos = minutos
        else:
            raise ValueError('Minutos em tempo negativo')
        
    

    def deposita_BH(self, minutos:int):
        '''
            Deposita os minutos extras no banco de horas.

        
        Exemplos:
        >>> h = BancoHoras(300)
        >>> h.consulta()
        '05:00'
        >>> h.deposita_BH(127)
        >>> h.consulta()
        '07:07'
        '''

        self.minutos += minutos



    def saque(self, minutos:int):
        '''
            Saca uma quantidade de minutos que um funcionario deseja se ausentar.

            Requer que o saldo seja maior que o valor do saque sugerido pelo funcionario.
        
        Exemplos:
        # Saldo Suficiente
        >>> h = BancoHoras(144)
        >>> h.consulta()
        '02:24'
        >>> h.saque(77)
        >>> h.consulta()
        '01:07'

        >>> h = BancoHoras(223)
        >>> h.consulta()
        '03:43'
        >>> h.saque(177)
        >>> h.consulta()
        '00:46'
        
        # Saldo Insuficiente
        >>> h = BancoHoras(144)
        >>> h.consulta()
        '02:24'
        >>> h.saque(222)
        Traceback (most recent call last):
        ...
        ValueError: Saque NEGADO! Saldo insuficiente!

        >>> h = BancoHoras(293)
        >>> h.consulta()
        '04:53'
        >>> h.saque(297)
        Traceback (most recent call last):
        ...
        ValueError: Saque NEGADO! Saldo insuficiente!

        '''

        if minutos < self.minutos:
            self.minutos -= minutos
        else:
            raise ValueError('Saque NEGADO! Saldo insuficiente!')



    def consulta(self) -> str:
        '''
            Mostra o banco de horas de um funcionario
        
        Exemplos:
        >>> h = BancoHoras(549)
        >>> h.consulta()
        '09:09'
        >>> h.saque(223)
        >>> h.consulta()
        '05:26'
        >>> h.deposita_BH(105)
        >>> h.consulta()
        '07:11'
        >>> h.deposita_BH(290)
        >>> h.consulta()
        '12:01'
        '''

        self.horas = self.minutos // 60
        self.resto_minutos = self.minutos % 60

        
        h_str = str(self.horas)
        m_str = str(self.resto_minutos)

        if self.horas < 10:
            h_str = '0' + h_str
        if self.resto_minutos < 10:
            m_str = '0' + m_str


        return f'{h_str}:{m_str}'