import heapq
from puzzle8 import tabuleiro

class AEstrela:
    def __init__(self, tabuleiro_inicial):
        self.inicial = tabuleiro_inicial
        self.objetivo = tabuleiro.OBJETIVO

    def executar(self):
        contador = 0
        
        h_inicial = tabuleiro.calcular_manhattan(self.inicial)
        # Inicialmente: g(n) = 0, então f(n) = h(n)
        open_list = [(h_inicial, contador, self.inicial, [])]
        
        visitados = set()
        
        while open_list:
            # Remove o estado com o menor f(n) da fila
            f_atual, _, estado_atual, caminho = heapq.heappop(open_list)
            
            # Critério de parada -> se a distância de Manhattan for 0, finaliza
            if tabuleiro.calcular_manhattan(estado_atual) == 0:
                return caminho
            
            estado_tuple = tuple(tuple(linha) for linha in estado_atual)
            if estado_tuple in visitados:
                continue
            visitados.add(estado_tuple)
            
            # Expandir todos os movimentos possíveis a partir do estado atual
            for mov in tabuleiro.MOVIMENTOS:
                proximo_estado = tabuleiro.aplicar_movimento(estado_atual, mov)
                
                # See for  um movimento valido, atualiza
                if proximo_estado != estado_atual:
                    proximo_tuple = tuple(tuple(linha) for linha in proximo_estado)
                    
                    if proximo_tuple not in visitados:
                        g_score = len(caminho) + 1
                        h_score = tabuleiro.calcular_manhattan(proximo_estado)
                        f_score = g_score + h_score
                        
                        contador += 1
                        # Adiciona a nova possibilidade na fila de prioridade
                        heapq.heappush(open_list, (f_score, contador, proximo_estado, caminho + [mov]))
                        
        print("[!] Não foi possível encontrar uma solução para este tabuleiro.")
        return None