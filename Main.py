from puzzle8 import tabuleiro
from algoritmos.alg_genetico import AlgoritmoGenetico
from algoritmos.alg_AEstrela import AEstrela


'''
é possivel alterar o tabuleiro la no arquivo tabuleiro.py, estão lá.

opcoes de tabuleiro: facil, medio, dificil, impossivel
'''
tabuleiro_teste = tabuleiro.tabuleiros["teste"]

def main():
    print("--- INICIANDO ALGORITMO GENÉTICO PARA 8-PUZZLE ---")
    print("Tabuleiro Inicial:")
    tabuleiro.imprimir_tabuleiro(tabuleiro_teste)
    
    dist_inicial = tabuleiro.calcular_manhattan(tabuleiro_teste)
    #print(f"Distancia Manhattan do inicio: {dist_inicial}\n")
    
    # Executa o AG
    ag = AlgoritmoGenetico(
        tabuleiro_inicial=tabuleiro_teste,
        tamanho_pop=800,          # População
        tamanho_cromossomo=90,    # Sequência
        geracoes=300,             
        tx_mutacao=0.1,
        tx_crossover=0.8
    )
    
    melhor_solucao = ag.executar()
    
    print("\nMelhor sequencia encontrada:", melhor_solucao)
    
    #imprimir resultado
    atual = tabuleiro_teste
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
            print("Melhor sequencia encontrada:", melhor_solucao)
            break
    
        
#------------------------------------------------------------------------#  
    print("\n--- INICIANDO ALGORITMO A* PARA 8-PUZZLE ---")
    print("Tabuleiro Inicial:")
    tabuleiro.imprimir_tabuleiro(tabuleiro_teste)
    
    # Executa o A*
    buscadorAE = AEstrela(tabuleiro_teste)
    melhor_solucaoAE = buscadorAE.executar()
    
    if melhor_solucaoAE:
        print(f"\nSolução ótima encontrada com {len(melhor_solucaoAE)} passos!")
        print("Sequência de movimentos:", melhor_solucaoAE)
        

if __name__ == "__main__":
    main()
