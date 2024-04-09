import psutil

# Variáveis de contagem
comps = trocas = passd = 0

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em seguida,
    encontra o menor valor no restante da lista. Se o valor
    encontrado for menor que o valor previamente selecionado,
    efetua a troca entre eles. Continuando, seleciona o segundo
    elemento da lista, buscando pelo menor valor nas posições
    subsequentes. Faz a troca entre os dois valores, se necessário.
    O processo se repete até que o penúltimo elemento da lista
    seja selecionado, comparado com o último e feita a troca entre
    eles, se for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop que vai da primeira até a PENÚLTIMA posição, para
    # selecionar o elemento que será comparado aos demais
    for pos_sel in range(len(lista) - 1):

        passd += 1

        # Inicia supondo que a posição do menor valor do resto
        # da lista é o que está imediatamente à frente do selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a pos_menor
        # até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor encontrado na posição pos for MENOR do que o
            # valor atual de pos_menor, então atualiza pos_menor para
            # a mesma posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <~ CUIDADO COM A INDENTAÇÃO!
        # Neste ponto, já terminamos de percorrer o restante da lista e
        # já sabemos a posição do menor elemento que há nele. Comparamos,
        # então, os valores das posições pos_menor e pos_sel. Se o
        # primeiro for MENOR do que o segundo, fazemos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

# Caso de teste
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print('ANTES:', nums)
selection_sort(nums)
print('DEPOIS:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

#############################################################
# TESTE COM 1M+ DE EMPRESAS

import sys
import time

sys.dont_write_bytecode = True  # Impede a criação do cache

# Importando a lista de empresas
import trabalho1.emp10mil as emp10mil

# Recortando os primeiros 10k nomes
empresas = emp10mil.empresas[:10000]

# Monitorando o uso de memória antes da ordenação
memoria_antes = psutil.virtual_memory().used

hora_ini = time.time()
selection_sort(empresas)
hora_fim = time.time()

# Monitorando o uso de memória após a ordenação
memoria_depois = psutil.virtual_memory().used

print(empresas)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Uso de memória antes da ordenação: {memoria_antes / (1024 * 1024):.2f} MB")
print(f"Uso de memória após a ordenação: {memoria_depois / (1024 * 1024):.2f} MB")
print(f"Memória utilizada durante a execução: {(memoria_depois - memoria_antes) / (1024 * 1024):.2f} MB")
