import copy

tabuleiros = {
    
    "objetivo": [  #tabuleiro objetivo -> apenas visual pois o manhattan calcula direto nos indices
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ],
    
    "facil" : [
        [1, 3, 5],
        [4, 2, 0],
        [7, 8, 6]
    ],

    "medio" : [
        [8, 2, 3],
        [1, 6, 4],
        [7, 0, 5]
    ],

    "dificil" : [
        [8, 6, 7],
        [2, 5, 4],
        [3, 0, 1]
    ],
    
    "impossivel": [ # sem solucao
        [8, 3, 6],
        [5, 4, 7],
        [2, 0, 1]
    ]
}

MOVIMENTOS = ['C', 'B', 'E', 'D']  # Cima, Baixo, Esquerda, Direita
PARES_OPOSTOS = {'C': 'B', 'B': 'C', 'E': 'D', 'D': 'E'}

def encontrar_vazio(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == 0:
                return i, j
    return 0, 0


#Veirifica se o movimento é valido, se não 'bate nos limites' e retorna a matriz nova ->  com as mudancas
def aplicar_movimento(matriz, movimento):
    nova_matriz = copy.deepcopy(matriz)
    i, j = encontrar_vazio(nova_matriz)
    
    novo_i, novo_j = i, j
    if movimento == 'C' and i > 0: novo_i -= 1
    elif movimento == 'B' and i < 2: novo_i += 1
    elif movimento == 'E' and j > 0: novo_j -= 1
    elif movimento == 'D' and j < 2: novo_j += 1
    
    # Realiza o swap se moveu
    if (novo_i, novo_j) != (i, j):
        nova_matriz[i][j], nova_matriz[novo_i][novo_j] = nova_matriz[novo_i][novo_j], nova_matriz[i][j]
        
    return nova_matriz

def calcular_manhattan(matriz):
    """
    Calcula a distância de Manhattan. 
    menor o valor = mais perto do objetivo
    """
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = matriz[i][j]
            if valor != 0:
                linha_correta = (valor - 1) // 3
                col_correta = (valor - 1) % 3
                distancia += abs(i - linha_correta) + abs(j - col_correta)
    return distancia

#Imprimir tabuleiro
def imprimir_tabuleiro(matriz):
    for linha in matriz:
        print(linha)
    print()
