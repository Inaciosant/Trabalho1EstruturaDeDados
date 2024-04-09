def quick_sort(lista, ini=0, fim=None):
    """
    Função que implementa o algoritmo Quick Sort de forma ITERATIVA
    """
    global passd, comps, trocas
    
    if fim is None: 
        fim = len(lista) - 1

    # Cria uma lista auxiliar
    tamanho = fim - ini + 1
    aux = [None] * tamanho
  
    # Inicializa a posição da lista auxiliar
    pos = -1
  
    # Coloca os valores iniciais de ini e fim na lista auxiliar
    pos += 1
    aux[pos] = ini
    pos += 1
    aux[pos] = fim
  
    # Continua retirando valores da lista auxiliar enquanto
    # ela não estiver vazia
    while pos >= 0:
  
        # Retira fim e início
        fim = aux[pos]
        pos -= 1
        ini = aux[pos]
        pos -= 1
  
        # Coloca o pivô em sua posição correta na lista ordenada
        i = ini - 1
        x = lista[fim]
    
        for j in range(ini, fim):
            comps += 1
            if lista[j] <= x:
                # Incrementa a posição do menor elemento
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas += 1
    
        lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
        
        pivot = i + 1
  
        # Se há elementos à esquerda do pivô, coloca-os
        # no lado esquerdo da lista auxiliar
        if pivot - 1 > ini:
            pos += 1
            aux[pos] = ini
            pos += 1
            aux[pos] = pivot - 1
  
        # Se há elementos à direita do pivô, coloca-os
        # no lado direito da lista auxiliar
        if pivot + 1 < fim:
            pos += 1
            aux[pos] = pivot + 1
            pos += 1
            aux[pos] = fim

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
