# Listas, Tuplas e Dicionários
# Listas [], Tuplas (), Dicionarios {}

## Listas
num = [2,5,7,9]
print(num)
num[3] = 4 # no lugar do elemento na posição 3 (numero 9) vai ser colocado o numero 4;
print(num)
num.append(8) # inclui o numero 8
num.sort() # coloca em ordem crescente
num.insert(2,0) # adiciona o zero na posicao 2
print(num)
num.remove(7)#remove o elemento 7
num.pop(3) #remove o elemento na posicao 3

## Tuplas (eh imutavel)
num2 = (2,5,7,9)
## nao eh possivel adicionar e modificar elementos numa tupla :C

## Dicionario {'chave':'valor'}

pessoas = {'nome':'fulano', 'sexo':'rock', 'idade': 49} # numero nao coloca aspas
pessoas['time'] = 'Vitoria' #adiciona mais uma chave e valor no dicionario
print(pessoas)
del pessoas['idade'] #deleta uma chave e valor
print(pessoas)

