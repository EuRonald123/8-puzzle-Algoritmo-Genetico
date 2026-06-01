from puzzle8 import tabuleiro
from algoritmos.alg_genetico import AlgoritmoGenetico


TABULEIRO_INICIAL = [
    [8, 2, 4],
    [0, 1, 6],
    [7, 5, 3]
]

def main():
    print("--- INICIANDO ALGORITMO GENÉTICO PARA 8-PUZZLE ---")
    print("Tabuleiro Inicial:")
    tabuleiro.imprimir_tabuleiro(TABULEIRO_INICIAL)
    
    dist_inicial = tabuleiro.calcular_manhattan(TABULEIRO_INICIAL)
    print(f"Distancia Manhattan do inicio: {dist_inicial}\n")
    
    # Executa o AG
    ag = AlgoritmoGenetico(
        tabuleiro_inicial=TABULEIRO_INICIAL,
        tamanho_pop=500,          # População
        tamanho_cromossomo=30,    # Sequência
        geracoes=500,             
        tx_mutacao=0.1,
        tx_crossover=0.8
    )
    
    melhor_solucao = ag.executar()
    
    print("\nMelhor sequencia encontrada:", melhor_solucao)
    
    #imprimir resultado
    atual = TABULEIRO_INICIAL
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
            print(">>> PARABÉNS! CHEGOU AO OBJETIVO! <<<")
            break

if __name__ == "__main__":
    main()
