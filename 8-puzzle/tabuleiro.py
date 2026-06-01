#Ideia
#Aqui vai ter os tabuleiros 8-puzzle -> Primeiro apenas um em ordem aleatório depois elaborar mais 2 tabuleiros
#Tabuleiro desejado / objetivo -> Para comparacao


#Tabuleiro objetivo sendo 0 o espaço vazio
OBJETIVO = [[1, 2, 3], 
            [4, 5, 6], 
            [7, 8, 0]]


TABULEIRO = [[5, 2, 7], 
             [0, 1, 6], 
             [3, 8, 4]]


#movimentos possiveis
#Observe que quem move é o espaço vazio, ou seja, os movimentos são referentes ao '0'
MOVIMENTOS = ['c', 'b', 'e', 'd']



#FUncao para encontrar o espaço vazio do nosso tabuleiro
def encontrar_vazio(matriz):
    tamanho = len(matriz)
    for i in range(tamanho):
        for j in range(tamanho):
            if matriz[i][j] == 0:
                return i, j


def aplicar_movimento(matriz, movimento):
    i, j = encontrar_vazio(matriz)

    #temporarios -> modificar eles e ve se mudou do original, só faz o swap
    temp_i, temp_j = i, j
    
    #movimento vertical
    if(movimento == 'c' and i > 0):
        temp_i -= 1
    elif(movimento == 'b' and i < 2):
        temp_i +=1
      
    #movimento horizontal  
    elif(movimento == 'e' and j > 0):
        temp_j -= 1
    elif(movimento == 'd' and j < 2):
        temp_j +=1
          
    #verificar se mudou alguma coisa
    if(temp_i, temp_j) != (i, j):
        i, j = temp_i, temp_j
    
    