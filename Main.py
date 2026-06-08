from puzzle8 import tabuleiro
from algoritmos.alg_genetico import AlgoritmoGenetico
from algoritmos.alg_AEstrela import AEstrela


#Alguns tabuleiros para testes

#facil
TABULEIRO_INICIAL_0 = [
    [1, 3, 5],
    [4, 2, 0],
    [7, 8, 6]
]

#medio
TABULEIRO_INICIAL_1 = [
    [8, 6, 7],
    [2, 5, 4],
    [3, 0, 1]
]

#dificil
TABULEIRO_INICIAL_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


def main():
    print("--- INICIANDO ALGORITMO GENÉTICO PARA 8-PUZZLE ---")
    print("Tabuleiro Inicial:")
    tabuleiro.imprimir_tabuleiro(TABULEIRO_INICIAL_0)
    
    dist_inicial = tabuleiro.calcular_manhattan(TABULEIRO_INICIAL_0)
    print(f"Distancia Manhattan do inicio: {dist_inicial}\n")
    
    # Executa o AG
    ag = AlgoritmoGenetico(
        tabuleiro_inicial=TABULEIRO_INICIAL_0,
        tamanho_pop=300,          # População
        tamanho_cromossomo=31,    # Sequência
        geracoes=300,             
        tx_mutacao=0.1,
        tx_crossover=0.8
    )
    
    melhor_solucao = ag.executar()
    
    print("\nMelhor sequencia encontrada:", melhor_solucao)
    
    #imprimir resultado
    atual = TABULEIRO_INICIAL_0
    print("\nExecutando Movimentos no Tabuleiro:")
    passos_uteis = 0
    for mov in melhor_solucao:
        proximo = tabuleiro.aplicar_movimento(atual, mov)
        # Se mudou, printa
        if proximo != atual:
            passos_uteis += 1
            print(f"Movimento {passos_uteis}: {mov}")
            tabuleiro.imprimir_tabuleiro(proximo)
            atual = proximo
            
        if tabuleiro.calcular_manhattan(atual) == 0:
            print(f"\nSolucao encontrada com {len(melhor_solucao)} passos!")
            break
    
    print("SOLUCAO NAO ENCONTRADA usando AG\n")
        
#------------------------------------------------------------------------#  
    print("\n--- INICIANDO ALGORITMO A* PARA 8-PUZZLE ---")
    print("Tabuleiro Inicial:")
    tabuleiro.imprimir_tabuleiro(TABULEIRO_INICIAL_0)
    
    # Executa o A*
    buscadorAE = AEstrela(TABULEIRO_INICIAL_0)
    melhor_solucaoAE = buscadorAE.executar()
    
    if melhor_solucaoAE:
        print(f"\nSolução ótima encontrada com {len(melhor_solucaoAE)} passos!")
        print("Sequência de movimentos:", melhor_solucaoAE)
        

if __name__ == "__main__":
    main()
