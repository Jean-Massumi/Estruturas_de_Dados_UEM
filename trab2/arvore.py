from __future__ import annotations
from dataclasses import dataclass

@dataclass
class No:
    esq: Arvore
    val: int
    dir: Arvore

Arvore = No | None

# Exercício 1

# Análise:
# Criar um ABB balanceada a partir de um arranjo de valores distintos em ordem crescente

def ABB(lst: list[int]) -> Arvore:
    '''
    Devolve uma ABB balanceada a partir do arranjo de entrada
    
    >>> ABB([3, 5, 7, 10, 12, 15])
    No(esq=No(esq=None, val=3, dir=No(esq=None, val=5, dir=None)), val=7,\
 dir=No(esq=No(esq=None, val=10, dir=None), val=12, dir=No(esq=None, val=15, dir=None)))
    >>> ABB([3, 5, 10, 12, 15])
    No(esq=No(esq=None, val=3, dir=No(esq=None, val=5, dir=None)), val=10,\
 dir=No(esq=None, val=12, dir=No(esq=None, val=15, dir=None)))
    '''

    def _auxilia(lst, inicio, fim) -> Arvore:
        if inicio > fim:
            return None
        else:
            meio = (inicio + fim) // 2
            raiz = No(None, lst[meio], None)

            raiz.esq = _auxilia(lst, inicio , meio - 1)
            raiz.dir = _auxilia(lst, meio + 1, fim)
        return raiz

    return _auxilia(lst, 0, len(lst) - 1)

print(ABB([3, 5, 7, 10, 12, 15]))


# Exercício 2

# Análise:
# Determinar se duas ABB's têm os mesmo elementos.

def ABBs_iguais(arv1: Arvore, arv2: Arvore) -> bool:
    '''
    Devolve True se a *arv1* têm os mesmo elementos de *arv2*. False, caso contrario.
    
    >>> ABBs_iguais(No(No(None, 3, None), 7, No(None, 11, None)), No(No(No(None, 3, None), 7, None), 11, None))
    True
    >>> ABBs_iguais(No(None, 5, No(None, 8, None)), No(No(None, 2, None), 5, No(None, 8, None)))
    False
    >>> ABBs_iguais(No(No(No(None, -3, None), 4, No(None, 5, None)), 7, No(No(None, 8, None), 9,\
 No(None, 12, None))), No(No(No(None, -3, None), 4, No(None, 5, None)), 7, No(No(None, 8, None), 9,\
 No(None, 12, None ))))
    True
    '''

    num_ele_arv1 = qtd_ele(arv1)
    num_ele_arv2 = qtd_ele(arv2)

    if num_ele_arv1 != num_ele_arv2:
        return False
   
    if arv1 is None:
        return None
    else:
        if percorre_ele(arv1, arv2.val):
            return ABBs_iguais(arv1, arv2.esq) or ABBs_iguais(arv1, arv2.dir)
        else:
            return True
     

# Auxilia a funcao ABBs_iguais
def qtd_ele(arv: Arvore) -> int:
    '''
    Devolve a quantitade de elemento de uma *Arvore*
    '''
    if arv is None:
        return 0
    else:
        return 1 + qtd_ele(arv.esq) + qtd_ele(arv.dir)


# Aulixia a função ABBs_iguais
def percorre_ele(arv: Arvore, val: int):
    '''
    Devolve True se o valor estiver na Arvore. Falsa, caso contraio.
    '''

    if arv is None:
        return None
    else:
        if val != percorre_ele(arv.esq, val) or val != percorre_ele(arv.dir, val):
            return False
    
    return True


# Exercício 3

# Anáise:
# Encontrar todos os caminhos de tamanho máximo, partindo da raiz.

def encontra_caminho(arv:Arvore) -> list:
    '''
    Devolve todos os caminhos de tamanho maximo da arvore.
    >>> encontra_caminho(None)
    []

    >>> encontra_caminho(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3,\
    No(No(None, 2, None), 5, None))))
    [[2, 8, 3, 4], [2, 3, 5, 2]]

    >>> encontra_caminho(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(No(None, 6, None),\
    7, None), 3, No(No(None, 2, None), 5, None))))
    [[2, 8, 3, 4], [2, 3, 7, 6], [2, 3, 5, 2]]

    >>> encontra_caminho(No(No(No(No(None, 1, None), 3, No(None, 4, None)), 8, None), 2,\
    No(No(No(None, 6, None), 7, None), 3, No(No(None, 2, None), 5, None))))
    [[2, 8, 3, 1], [2, 8, 3, 4], [2, 3, 7, 6], [2, 3, 5, 2]]

    >>> encontra_caminho(No(No(No(No(None, 1, None), 3, No(None, 4, None)), 8, None), 2,\
    No(No(No(None, 6, None), 7, None), 3, No(No(None, 2, None), 5, No(None, 11, None)))))
    [[2, 8, 3, 1], [2, 8, 3, 4], [2, 3, 7, 6], [2, 3, 5, 2], [2, 3, 5, 11]]

    Árvore do exemplo 2
          2                 
        /   \               
      8      3              
     /      / \             
    3      7   5
     \        /             
      4      2        

    Árvore do exemplo 3
          2
        /   \
      8      3
     /      / \
    3      7   5
     \    /   /
      4  6   2      

    Árvore do exemplo 4  
            2
          /   \
        8      3
       /      / \
      3      7   5
     / \    /   /
    1   4  6   2 
    
    Árvore do exemplo 5
            2
          /   \
        8      3
       /      / \
      3      7   5
     / \    /   / \
    1   4  6   2  11
    
    '''

    if arv is None:
        return []
    
    # Variavel que irá guarda todos os caminhos maximos. 
    caminho = []
    # Variavel que guarda a altura da arvore
    altura_arvore = altura(arv)

    def encontra_caminho_esquerda(arv:Arvore, atual_caminho:list, raiz: int):
        '''
        Encontra todos os caminhos máximos da esquerda
        '''
        if arv is None:
            return None
        
        # Condição para armazenar a raiz principal da arvore.
        if atual_caminho == []:
            atual_caminho.append(raiz)
        
        atual_caminho.append(arv.val)

        # Variavel para guarda os elementos do caminho caso haja duas opção: esquerda
        # ou direita.
        novos_caminhos = atual_caminho.copy()

        # Condição ,caso haja dois dois caminhos.
        if arv.esq is not None and arv.dir is not None:
            encontra_caminho_esquerda(arv.esq, atual_caminho, raiz)
            encontra_caminho_direita(arv.dir, novos_caminhos, raiz)
 
        # Condição para verificar, se a quantidade de elementos de uma lista é igual a 
        # altura da arvore
        if len(novos_caminhos) == altura_arvore:
            caminho.append(novos_caminhos.copy())
            if len(caminho) > 1:
                if caminho[-1] == caminho[- 2]:
                    caminho.pop()
    
        elif (arv.esq is None and arv.dir is None) and len(atual_caminho) < altura_arvore:
            atual_caminho.pop()


        encontra_caminho_esquerda(arv.esq, atual_caminho, raiz)
        encontra_caminho_esquerda(arv.dir, atual_caminho, raiz)
    

    def encontra_caminho_direita(arv:Arvore, atual_caminho:list, raiz: int):
        '''
        Encontra todos os caminhos máximos da direita
        '''

        if arv is None:
            return None
        
        if atual_caminho == []:
            atual_caminho.append(raiz)
        
        atual_caminho.append(arv.val)

        novos_caminhos = atual_caminho.copy()

        if arv.esq is not None and arv.dir is not None:
            encontra_caminho_esquerda(arv.esq, atual_caminho, raiz)
            encontra_caminho_direita(arv.dir, novos_caminhos, raiz)


        if len(novos_caminhos) == altura_arvore:
            caminho.append(novos_caminhos.copy())
            if len(caminho) > 1:
                if caminho[-1] == caminho[- 2]:
                    caminho.pop()

        elif (arv.esq is None and arv.dir is None) and len(atual_caminho) < altura_arvore:
            atual_caminho.pop()


        encontra_caminho_direita(arv.esq, atual_caminho, raiz)
        encontra_caminho_direita(arv.dir, atual_caminho, raiz)


    encontra_caminho_esquerda(arv.esq, [], arv.val)
    encontra_caminho_direita(arv.dir, [], arv.val)


    return caminho


def altura(arv: Arvore) -> int:
    '''
    Calcula e devolve a altura da arvore.
    >>> altura(No(No(No(None, 3, No(None, 4, None)), 8, None), 2, No(No(None, 7, None), 3,\
    No(No(None, 2, None), 5, None))))
    4
    '''

    if arv is None:
        return 0
    elif altura(arv.esq) > altura(arv.dir):
        return 1 + altura(arv.esq)
    else:
        return 1 + altura(arv.dir)
    

print(encontra_caminho(No(No(No(No(None, 1, None), 3, No(None, 4, None)), 8, None), 2,\
    No(No(No(None, 6, None), 7, None), 3, No(No(None, 2, None), 5, No(None, 11, None))))))
