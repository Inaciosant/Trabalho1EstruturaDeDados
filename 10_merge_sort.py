import psutil

# Variáveis de contagem
divs = juncs = comps = 0

def merge_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO MERGE SORT
    No processo de ordenação, este algoritmo "desmonta"
    a lista original, contendo N elementos, até obter
    N listas com apenas um elemento cada uma. Em seguida,
    usando a técnica de mesclagem (merging), "remonta" a
    lista, desta vez com os elementos já em ordem.
    """
    global divs, juncs, comps

    # Para que possa haver divisão da lista, esta deve ter
    # mais de um elemento
    if len(lista) > 1:

        # Encontra a posição do meio da lista, para fazer
        # a divisão em duas metades
        meio = len(lista) // 2

        # Tira uma cópia da primeira metade da lista
        sublista_esq = lista[:meio]
        # Tira uma cópia da segunda metade da lista
        sublista_dir = lista[meio:]

        divs += 1

        # Chamamos recursivamente a própria função para que
        # ela continue repartindo cada sublista em duas
        # partes menores
        sublista_esq = merge_sort(sublista_esq)
        sublista_dir = merge_sort(sublista_dir)

        # PARTE 2: REMONTAGEM DA LISTA, DE FORMA ORDENADA

        pos_esq = pos_dir = 0
        ordenada = []       # Lista vazia

        while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

            comps += 1

            # O menor elemento está na sublista da esquerda
            if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
                # "Desce" o elemento da esquerda para a lista ordenada
                ordenada.append(sublista_esq[pos_esq])
                pos_esq += 1
            # O menor elemento está na sublista da direita
            else:
                # "Desce" o elemento da direita para a lista ordenada
                ordenada.append(sublista_dir[pos_dir])
                pos_dir += 1

        # Verificação da sobra
        sobra = []

        # Sobra à esquerda
        if pos_esq < len(sublista_esq): 
            sobra = sublista_esq[pos_esq:]
        # Sobra à direita
        elif pos_dir < len(sublista_dir): 
            sobra = sublista_dir[pos_dir:]

        juncs += 1

        # O resultado final é a junção (concatenação) da lista
        # ordenada com a sobra
        return ordenada + sobra
    
    else:
        return lista
    
########################################################################

#nums = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#print('ANTES:', nums)
#nums_ord = merge_sort(nums.copy())
#print('DEPOIS:', nums_ord)
#print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")

#############################################################
# TESTE COM 1M+ DE EMPRESAS

import sys
import tracemalloc
from time import time

# Importando a lista de empresas
from trabalho1.emp10mil import empresas


# Recortando os primeiros 10k empresas
#empresas = empresas[:10000]

divs = juncs = comps = 0

tracemalloc.start()         # Inicia medição do consumo de memória
hora_ini = time()
empresas_ord = merge_sort(empresas.copy())
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()          # Termina a medição de memória

print(empresas_ord[:10])    # Lista após ordenação (mostrando os 10 primeiros)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Divisões: {divs}, junções: {juncs}, comparações: {comps}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")
