# Variáveis de contagem
passd = comps = trocas = 0

def quick_sort(lista, ini=0, fim=None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô
    (na nossa implementação, será o último) e, na primeira
    passada, divide a lista, a partir da posição final do
    pivô, em uma sublista à esquerda, contendo apenas
    valores menores que o pivô, e outra sublista à direita,
    contendo apenas valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada
    uma das sublistas, até que toda a lista esteja ordenada.
    """
    global passd, comps, trocas

    if fim is None:
        fim = len(lista) - 1

    if fim <= ini:
        return

    pivot = fim
    div = ini - 1
    passd += 1

    for pos in range(ini, fim):
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1
            if pos != div:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    div += 1

    if div != pivot:
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1

    quick_sort(lista, ini, div - 1)
    quick_sort(lista, div + 1, fim)

############################################################

import sys
import tracemalloc
from time import time

# Inicializando variáveis de contagem
passd = comps = trocas = 0

# Inicializando tracemalloc
tracemalloc.start()

# Importando a lista de empresas
from trabalho1.emp10mil import empresas

# Início da contagem de tempo
hora_ini = time()

# Ordenação da lista
quick_sort(empresas)

# Fim da contagem de tempo
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()

# Finaliza o tracemalloc
tracemalloc.stop()

print(empresas[:10])    # Lista após ordenação (mostrando os 10 primeiros)
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")
