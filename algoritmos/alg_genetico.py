import random
from puzzle8 import tabuleiro

class AlgoritmoGenetico:
    def __init__(self, tabuleiro_inicial, tamanho_pop=150, tamanho_cromossomo=35, geracoes=500, tx_mutacao=0.1, tx_crossover=0.8):
        self.inicial = tabuleiro_inicial
        self.tamanho_pop = tamanho_pop
        self.tamanho_cromossomo = tamanho_cromossomo
        self.geracoes = geracoes
        self.tx_mutacao = tx_mutacao
        self.tx_crossover = tx_crossover
        
        
    #Cria indivíduos representados por uma sequência de movimentos (Genes)."""
    def criar_populacao_inicial(self):
        populacao = []
        for _ in range(self.tamanho_pop):
            #evitar criar movimentos burros repetidos inicialmente
            cromossomo = [random.choice(tabuleiro.MOVIMENTOS)]
            for _ in range(1, self.tamanho_cromossomo):
                prox = random.choice(tabuleiro.MOVIMENTOS)
                # evitaadicionar um movimento oposto ao anterior para evitar andar e voltar
                while prox == tabuleiro.PARES_OPOSTOS[cromossomo[-1]]:
                    prox = random.choice(tabuleiro.MOVIMENTOS)
                cromossomo.append(prox)
            populacao.append(cromossomo)
        return populacao

    def avaliar_fitness(self, cromossomo):
        """
        O fitness baseia-se em quão próximo o tabuleiro fica do objetivo
        Aplica a sequência no tabuleiro e tira a melhor (menor) distância de Manhattan encontrada no caminho.
        Quanto mais perto de 0 o fitness, MELHOR.
        """
        estado_atual = self.inicial
        melhor_distancia = tabuleiro.calcular_manhattan(estado_atual)
        
        for mov in cromossomo:
            estado_atual = tabuleiro.aplicar_movimento(estado_atual, mov)
            dist_atual = tabuleiro.calcular_manhattan(estado_atual)
            
            if dist_atual < melhor_distancia:
                melhor_distancia = dist_atual

            # Se achar a solução no meio do caminho, já pode parar
            if melhor_distancia == 0:
                break
                
        return melhor_distancia

    def selecao_por_torneio(self, populacao, fitness_populacao, k=3):
        """
        Seleção POR DISPUTA (Torneio):
        Sorteamos 'k' indivíduos aleatórios da população.
        Eles "disputam" e o que tiver o MELHOR fitness (menor valor) vence para virar pai/mãe.
        """
        selecionados = random.choices(list(zip(populacao, fitness_populacao)), k=k)
        # Escolhe o que tem menor fitness
        vencedor = min(selecionados, key=lambda x: x[1])
        return vencedor[0] # Retorna o cromossomo vencedor

    def crossover(self, pai1, pai2):
        """Crossover de 1 ponto: corta, mistura o início de um com o final de outro."""
        if random.random() > self.tx_crossover:
            return pai1[:], pai2[:]  # Não faz crossover
            
        ponto = random.randint(1, self.tamanho_cromossomo - 1)
        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]
        
        return filho1, filho2
    
    #Altera alguns movimentos (genes) do indivíduo com base na taxa de mutação
    def mutacao(self, cromossomo, taxa=None):
        taxa_aplicada = taxa if taxa is not None else self.tx_mutacao
        novo_cromo = cromossomo[:]
        for i in range(len(novo_cromo)):
            if random.random() < taxa_aplicada:
                novo_cromo[i] = random.choice(tabuleiro.MOVIMENTOS)
        return novo_cromo

    def executar(self):
        populacao = self.criar_populacao_inicial()
        
        melhor_fit_global = float('inf')
        estagnacao = 0
        
        # Elitismo: sempre carrega o melhor da geração anterior
        for gen in range(self.geracoes):
            # 1. Avalia todo mundo
            fitness_pop = [self.avaliar_fitness(ind) for ind in populacao]
            
            melhor_idx = fitness_pop.index(min(fitness_pop))
            melhor_ind = populacao[melhor_idx]
            melhor_fit = fitness_pop[melhor_idx]
            
            #CONTROLE DE ESTAGNAÇÃO -> (Evitar Mínimo Local)
            if melhor_fit < melhor_fit_global:
                melhor_fit_global = melhor_fit
                estagnacao = 0  # Zerou a estagnação
            else:
                estagnacao += 1 # Não melhorou
                
            print(f"Geração {gen} | Melhor Distância: {melhor_fit} | Estagnação: {estagnacao}/50")
            
            # 2. Critério de Parada
            if melhor_fit == 0:
                print(f"\n[!] SOLUÇÃO ENCONTRADA na Geração {gen}!")
                return melhor_ind
                
            # a partir daqui já é brisa minha, tentei adicionar formas para sair dos mínimos locais mas nao funfou
            #TÉCNICA 1: CATACLISMO -> Diversidade extrema
            if estagnacao >= 50:
                print("   [!] MÍNIIMO LOCAL DETECTADO! Renovando (95%) da população")
                populacao_nova_aleatoria = self.criar_populacao_inicial()
                # Mantém o melhor e um punhado pra não perder tudo
                populacao = [melhor_ind] * 5 + populacao_nova_aleatoria[5:]
                estagnacao = 0
                continue
                
            #TÉCNICA 2 -> MUTAÇÃO ADAPTATIVA ---
            # Se estiver travado ha mais de 15 turnos -> aumenta a mutação para explorar caminhos novos
            tx_mut_atual = self.tx_mutacao
            if estagnacao > 15:
                tx_mut_atual = 0.4 # Sobe para 40%
                
            nova_populacao = []
            
            # Mantém o melhor absoluto
            nova_populacao.append(melhor_ind)
            
            # 3. Montar a nova geração (Seleção e Reprodução)
            while len(nova_populacao) < self.tamanho_pop:
                # Disputa dos pais
                pai = self.selecao_por_torneio(populacao, fitness_pop)
                mae = self.selecao_por_torneio(populacao, fitness_pop)
                
                # Crossover
                filho1, filho2 = self.crossover(pai, mae)
                
                # Mutação (usando a taxa adaptativa controlada)
                filho1 = self.mutacao(filho1, taxa=tx_mut_atual)
                filho2 = self.mutacao(filho2, taxa=tx_mut_atual)
                
                nova_populacao.extend([filho1, filho2])
                
            # Garante tamanho exato
            populacao = nova_populacao[:self.tamanho_pop]

        print("\n[!] Limite de gerações atingido. O algoritmo não chegou ao zero perfeito.")
        return melhor_ind
