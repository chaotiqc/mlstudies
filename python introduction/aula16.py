# Vetores (arrays) e Matrizes
## matriz contem n-linhas e n-colunas
## vetores é uma matriz unidimensional tendo só uma coluna ou só uma linha

vetor = [2,4,5,6]
print(type(vetor))
matriz =[[1,2,3],
         [4,5,6],
         [7,8,9]]
print(type(matriz))
print(matriz) #printa em formato de lista

# usando o numpy e o array

import numpy as np
vetor2 = np.array([1, -3, 4.2, 5]) #armazena como array
print(type(vetor2))
print(vetor2)

matriz2 = np.ones((2,3)) #vai criar uma matriz 2x3 com valores iguais a 1
print(type(matriz2))
print(matriz2)

matriz3 = np.diag((2,4,6,8,10)) #matriz diagonal, em que os valores da diagonal sao os parametros escritos dentro da funcao
print(matriz3)
print(type(matriz3))