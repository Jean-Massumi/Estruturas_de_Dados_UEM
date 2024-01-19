class BancoHoras:
    '''
        Registro/consulta de horas extras depositados em um banco de horas
    '''


    def __init__(self, horas, minutos):
        '''
            Cria um armazenamento de horas extra e minutos extras de um funcionario.

            As horas e minutos serao representados por valores inteiros positivos.

            Requer que minutos nao seja >= que 60            

        Exemplos:
        >>> h = BancoHoras(2, 24)
        >>> h.consulta()
        '02:24'
        >>> h = BancoHoras(5, 80)
        Traceback (most recent call last):
        ...
        ValueError: A margem de minutos foi excedido
    
        '''
    
        
        if minutos >= 60:
            raise ValueError('A margem de minutos foi excedido')
        else:
            self.horas = horas
            self.banco_minutos = minutos


    def deposita_BH(self, horas_depositadas, minutos_depositados):
        '''
            Deposita as horas extras e minutos extras no banco de horas e minutos respectivamente.

        
        Exemplos:
        >>> h = BancoHoras(2, 24)
        >>> h.consulta()
        '02:24'
        >>> h.deposita_BH(1, 56)
        >>> h.consulta()
        '04:20'
        '''

        self.horas += horas_depositadas
        self.banco_minutos += minutos_depositados
    
        if self.banco_minutos >= 60:
            self.banco_minutos = self.banco_minutos % 60
            self.horas += 1
    


    def saque(self, saque_horas, saque_minutos):
        '''
            Saca uma quantidade de horas e minutos que um funcionario deseja se ausentar.

            Requer que o saldo seja maior que o valor do saque sugerido pelo funcionario.
        
        Exemplos:
        # Saldo Suficiente
        >>> h = BancoHoras(2, 24)
        >>> h.consulta()
        '02:24'
        >>> h.saque(1, 17)
        >>> h.consulta()
        '01:07'

        >>> h = BancoHoras(3, 43)
        >>> h.consulta()
        '03:43'
        >>> h.saque(2, 57)
        >>> h.consulta()
        '00:46'
        
        # Saldo Insuficiente
        >>> h = BancoHoras(2, 24)
        >>> h.consulta()
        '02:24'
        >>> h.saque(3, 42)
        Traceback (most recent call last):
        ...
        ValueError: Saque NEGADO! Saldo insuficiente!

        >>> h = BancoHoras(4, 53)
        >>> h.consulta()
        '04:53'
        >>> h.saque(4, 57)
        Traceback (most recent call last):
        ...
        ValueError: Saque NEGADO! Saldo insuficiente!

        '''

        if (saque_horas < self.horas) and (saque_minutos != self.banco_minutos) or \
                ((saque_horas == self.horas) and (saque_minutos == self.banco_minutos)):
           
            if saque_minutos > self.banco_minutos:
                self.horas -= saque_horas + 1
                self.banco_minutos += 60 - saque_minutos

            else:
                self.horas -= saque_horas
                self.banco_minutos -= saque_minutos

        else:
            raise ValueError('Saque NEGADO! Saldo insuficiente!')


    def consulta(self) -> str:
        '''
            Mostra o banco de horas de um funcionario
        
        Exemplos:
        >>> h = BancoHoras(9, 9)
        >>> h.consulta()
        '09:09'
        >>> h.saque(3, 43)
        >>> h.consulta()
        '05:26'
        >>> h.deposita_BH(1, 45)
        >>> h.consulta()
        '07:11'
        >>> h.deposita_BH(4, 50)
        >>> h.consulta()
        '12:01'
        '''

        h_str = str(self.horas)
        m_str = str(self.banco_minutos)

        if self.horas < 10:
            h_str = '0' + h_str
        if self.banco_minutos < 10:
            m_str = '0' + m_str


        return f'{h_str}:{m_str}'
