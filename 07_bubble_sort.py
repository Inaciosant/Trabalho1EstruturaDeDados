import psutil

# Variáveis de contagem
comps = trocas = passd = 0

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR do que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido efetuada.    
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop eterno; não sabemos antecipadamente quantas passadas
    # serão necessárias
    while True:
        passd += 1

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        for pos in range(len(lista) - 1):

            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # efetuamos uma TROCA
            if lista[pos + 1] < lista[pos]:
                # Troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True   # Houve troca na passada

            comps += 1

        # Se não houve trocas na passada, a lista está ordenada
        # e interrompemos o loop eterno while True
        # <~ CUIDADO COM A INDENTAÇÃO
        if not trocou:
            break

# Caso de teste
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('ANTES:', nums)
bubble_sort(nums)
print('DEPOIS:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

# TESTE COM 1M+ DE EMPRESAS
import sys
import time

sys.dont_write_bytecode = True  # Impede a criação do cache

# Importando a lista de empresas
from trabalho1.emp10mil import empresas  # Importando a lista 'empresas' do arquivo emp10mil.py

# Recortando as primeiras 10k empresas
empresas = empresas[:10000]

# Monitorando o uso de memória antes da ordenação
memoria_antes = psutil.virtual_memory().used

hora_ini = time.time()
bubble_sort(empresas)
hora_fim = time.time()

# Monitorando o uso de memória após a ordenação
memoria_depois = psutil.virtual_memory().used

print(empresas)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Uso de memória antes da ordenação: {memoria_antes / (1024 * 1024):.2f} MB")
print(f"Uso de memória após a ordenação: {memoria_depois / (1024 * 1024):.2f} MB")
print(f"Memória utilizada durante a execução: {(memoria_depois - memoria_antes) / (1024 * 1024):.2f} MB")
